#!/usr/bin/env python3
"""
Generate a blog-like website from Jupyter notebooks.
"""

import json
import os
import glob
from pathlib import Path
import shutil
import html
from datetime import datetime
import markdown
from yattag import Doc
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import base64
import re


def find_notebooks():
    """Find all Jupyter notebooks in the current directory."""
    return glob.glob("*.ipynb")


def parse_notebook(notebook_path):
    """Parse a Jupyter notebook and extract content."""
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    cells = notebook.get("cells", [])
    title = None
    content_blocks = []

    for cell in cells:
        cell_type = cell.get("cell_type")
        source = cell.get("source", [])

        if isinstance(source, list):
            source_text = "".join(source)
        else:
            source_text = source

        if cell_type == "markdown":
            # Extract title from first markdown cell if it contains h1
            if title is None and source_text.startswith("# "):
                title = source_text.split("\n")[0][2:].strip()

            content_blocks.append({"type": "markdown", "content": source_text})

        elif cell_type == "code":
            outputs = cell.get("outputs", [])

            # Process code cell
            content_blocks.append(
                {"type": "code", "content": source_text, "outputs": outputs}
            )

    # If no title found, use filename
    if title is None:
        title = Path(notebook_path).stem.replace("_", " ").replace("-", " ").title()

    return {
        "title": title,
        "filename": Path(notebook_path).stem,
        "content_blocks": content_blocks,
    }


def process_output(output, output_dir, image_counter):
    """Process a cell output and convert to HTML."""
    output_type = output.get("output_type")

    if output_type == "execute_result" or output_type == "display_data":
        data = output.get("data", {})

        # Image output (PNG, JPEG, etc.)
        if "image/png" in data:
            image_data = data["image/png"]
            # Remove any newlines from base64 data
            image_data = re.sub(r"\s+", "", image_data)
            try:
                # Decode base64 image data
                image_bytes = base64.b64decode(image_data)
                # Generate filename
                image_filename = f"image_{image_counter[0]}.png"
                image_path = output_dir / "assets" / image_filename
                # Save image
                with open(image_path, "wb") as f:
                    f.write(image_bytes)
                image_counter[0] += 1
                return f'<img src="/assets/{image_filename}" alt="Generated plot" style="max-width: 100%; height: auto;" />'
            except Exception as e:
                print(f"Warning: Failed to decode image: {e}")
                return f'<p class="error">Failed to load image</p>'

        # HTML output
        elif "text/html" in data:
            return "".join(data["text/html"])

        # Plain text output
        elif "text/plain" in data:
            text = "".join(data["text/plain"])
            return f'<pre class="output">{html.escape(text)}</pre>'

    elif output_type == "stream":
        text = "".join(output.get("text", []))
        return f'<pre class="output">{html.escape(text)}</pre>'

    elif output_type == "error":
        error_name = output.get("ename", "Error")
        error_value = output.get("evalue", "")
        return f'<pre class="error"><strong>{error_name}:</strong> {html.escape(error_value)}</pre>'

    return ""


def generate_page_html(notebook_data, all_notebooks, output_dir):
    """Generate HTML for a single notebook page using yattag."""
    doc, tag, text = Doc().tagtext()

    # Counter for image numbering
    image_counter = [0]

    # Find home notebook for navbar
    home_exists = any(nb["filename"] == "home" for nb in all_notebooks)

    with tag("html", lang="en"):
        with tag("head"):
            with tag("meta", charset="UTF-8"):
                pass
            with tag(
                "meta", name="viewport", content="width=device-width, initial-scale=1.0"
            ):
                pass
            with tag("title"):
                text(notebook_data["title"])
            with tag("link", rel="stylesheet", href="style.css"):
                pass

        with tag("body"):
            with tag("div", klass="header"):
                with tag("div", klass="navigation"):
                    if home_exists:
                        with tag("a", href="index.html"):
                            text("Home")

            with tag("div", klass="content"):
                # Process content blocks
                for block in notebook_data["content_blocks"]:
                    if block["type"] == "markdown":
                        # Use markdown library to convert to HTML
                        md_html = markdown.markdown(block["content"])
                        doc.asis(md_html)

                    elif block["type"] == "code":
                        # Code input with syntax highlighting
                        code_content = block["content"]
                        if code_content.strip():
                            # Use Pygments for syntax highlighting
                            formatter = HtmlFormatter(
                                style="default", cssclass="highlight"
                            )
                            highlighted = highlight(
                                code_content, PythonLexer(), formatter
                            )
                            with tag("div", klass="code-input"):
                                doc.asis(highlighted)
                        else:
                            with tag("pre", klass="code-input"):
                                with tag("code"):
                                    text(code_content)

                        # Code outputs
                        for output in block["outputs"]:
                            output_html = process_output(
                                output, output_dir, image_counter
                            )
                            if output_html:
                                with tag("div", klass="code-output"):
                                    doc.asis(output_html)

            with tag("div", klass="footer"):
                text(f"Last updated: • {datetime.now().strftime('%Y-%m-%d')}")

    return doc.getvalue()


def generate_index_page(all_notebooks, output_dir):
    """Generate an index page listing all notebooks."""
    # Find home notebook or create a default index
    home_notebook = None
    for nb in all_notebooks:
        if nb["filename"] == "home":
            home_notebook = nb
            break

    if home_notebook:
        return generate_page_html(home_notebook, all_notebooks, output_dir)

    # Generate default index using yattag
    doc, tag, text = Doc().tagtext()

    with tag("html", lang="en"):
        with tag("head"):
            with tag("meta", charset="UTF-8"):
                pass
            with tag(
                "meta", name="viewport", content="width=device-width, initial-scale=1.0"
            ):
                pass
            with tag("title"):
                text("Notebook Website")
            with tag("link", rel="stylesheet", href="style.css"):
                pass

        with tag("body"):
            with tag("div", klass="header"):
                with tag("div", klass="navigation"):
                    with tag("a", href="index.html"):
                        text("Home")

            with tag("h1"):
                text("Notebook Website")

            with tag("p"):
                text(
                    "Welcome to this notebook-generated website. Here are the available pages:"
                )

            with tag("ul", klass="notebook-list"):
                for nb in all_notebooks:
                    with tag("li"):
                        with tag("a", href=f"{nb['filename']}.html"):
                            text(nb["title"])

            with tag("div", klass="footer"):
                text(f"Last update: • {datetime.now().strftime('%Y-%m-%d')}")

    return doc.getvalue()


def main():
    """Main function to generate the website."""
    print("🚀 Generating website from Jupyter notebooks...")

    # Find all notebooks
    notebook_files = find_notebooks()
    if not notebook_files:
        print("❌ No Jupyter notebooks found in current directory!")
        return

    print(f"📚 Found {len(notebook_files)} notebook(s): {', '.join(notebook_files)}")

    # Parse all notebooks
    all_notebooks = []
    for notebook_file in notebook_files:
        try:
            notebook_data = parse_notebook(notebook_file)
            all_notebooks.append(notebook_data)
            print(f"✅ Parsed: {notebook_file} -> {notebook_data['title']}")
        except Exception as e:
            print(f"❌ Error parsing {notebook_file}: {e}")

    if not all_notebooks:
        print("❌ No notebooks could be parsed!")
        return

    # Create output directory
    output_dir = Path("dist")
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir()
    shutil.copytree("assets", output_dir / "assets")

    # Create CSS file
    shutil.copy("style.css", "dist/style.css")

    # Generate pages
    for notebook_data in all_notebooks:
        html_content = generate_page_html(notebook_data, all_notebooks, output_dir)

        # Determine filename
        if notebook_data["filename"] == "home":
            output_file = output_dir / "index.html"
        else:
            output_file = output_dir / f"{notebook_data['filename']}.html"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"📄 Generated: {output_file}")

    # Generate index page if no home notebook exists
    home_exists = any(nb["filename"] == "home" for nb in all_notebooks)
    if not home_exists:
        index_html = generate_index_page(all_notebooks, output_dir)
        with open(output_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(index_html)
        print("📄 Generated: dist/index.html")

    print(f"🎉 Website generated successfully in '{output_dir}' directory!")
    print(f"💡 Open dist/index.html in your browser to view the site.")


if __name__ == "__main__":
    main()
