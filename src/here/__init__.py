import datetime
import os
import shutil
from pathlib import Path

import marimo
import polars as pl
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
from marimo._server.file_router import AppFileRouter
from marimo._utils.marimo_path import MarimoPath
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

load_dotenv()
PATH_WEB = Path(__file__).parent.parent.parent / "web"
PATH_PAGES = Path(__file__).parent.parent.parent / "pages"
PATH_ASSETS = Path(__file__).parent.parent.parent / "assets"
PATH_TEMPLATES = Path(__file__).parent / "templates"
if "PROJECT_DIR" in os.environ:
    PROJECTS = Path(os.environ["PROJECT_DIR"])
else:
    PROJECTS = None

# Home page URL constant
HOME_PAGE_URL = "/index.html"


def compute_age(birth_date) -> int:
    today = datetime.date.today()
    years = today.year - birth_date.year
    if today.month < birth_date.month or (
        today.month == birth_date.month and today.day < birth_date.day
    ):
        years -= 1
    return years


def me():
    birth_date = datetime.date(2003, 8, 18)
    age = compute_age(birth_date)
    name = "Antonin"
    alias = "rambip"
    return pl.DataFrame([{"age": age, "name": name, "alias": alias}])


CELL_TEMPLATE_MD = """
@app.cell(hide_code=True)
def _(mo):
    mo.md(r\"\"\"
{md}
\"\"\")
"""


INIT = """
import marimo
app = marimo.App(width="medium")
@app.cell
def _():
    import marimo as mo
    return (mo,)
"""

EXPORT = """
@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "{description}")
"""

IMPORT = """
@app.cell
def _():
    import {name}
    {name}.page_()
"""


def setup_everything():
    basepath = Path("/mnt/data/Proj/my-web-journal/journals")

    names = []

    for x in basepath.glob("*.md"):
        if not x.is_file():
            continue
        name = "journal_" + x.name.split(".")[0]
        names.append(name)
        new = PATH_PAGES / f"{name}.py"
        with open(x, "r") as f1:
            content = f1.read()
            title = content.split("\n")[0]
            with open(new, "w") as f2:
                content = map(
                    lambda x: x.replace("\n  ", "\n").replace("\t", "    "),
                    content.split("\n- "),
                )

                f2.write(INIT)
                f2.write(EXPORT.format(description=title))
                for c in content:
                    f2.write(CELL_TEMPLATE_MD.format(md=c))
        with open(PATH_PAGES / "journals.py", "w") as f:
            f.write(INIT)
            f.write(EXPORT.format(description="My blogposts"))
            for name in names:
                f.write(IMPORT.format(name=name))


def get_cells(path: Path):
    # Create a file router
    m_path = MarimoPath(path)
    file_router = AppFileRouter.from_filename(m_path)
    file_key = file_router.get_unique_file_key()
    assert file_key is not None

    # Use the file path directly for configuration
    # config = get_default_config_manager(current_path=str(path))
    return file_router.get_file_manager(file_key).app.cell_manager.cell_data()


# @marimo.persistent_cache
def generate_html(template_str, path, app, python_content, url=None):
    cells = get_cells(path)
    outputs = [x._repr_html_() if x is not None else None for x in app.run()[0]]
    lexer = PythonLexer()
    formater = HtmlFormatter()
    code = [
        highlight(c.code, lexer, formater) if not c.config.hide_code else None
        for c in cells
    ]
    content = list(zip(code, outputs))

    env = Environment(loader=FileSystemLoader(PATH_TEMPLATES))
    template = env.get_template("main.html")

    return template.render(
        name=url,
        content=content,
        home_page_url=HOME_PAGE_URL,
        python_content=python_content,
        python_filename=path.name,
    )


def include(path_str, app, link_name, url=None):
    if marimo.running_in_notebook():
        return marimo.Html('<span style="color:orange">file not included</span>')

    path = Path(path_str)

    # Render the template
    if url is None:
        url = f"{path.name}.html"
    assert path.parent.name == "pages"
    dist_folder = path.parent.parent / "web"
    dist_folder.mkdir(exist_ok=True)

    # Read the Python file content
    with open(path, "r") as f:
        python_content = repr(f.read())

    with open(PATH_TEMPLATES / "main.html") as f:
        template_str = f.read()

    html_content = generate_html(template_str, path, app, python_content, url=url)

    with open(dist_folder / url, "w") as f:
        f.write(html_content)

    return marimo.Html(f'<a href="/{url}">{link_name}</a>')


def asset(relative_path: str):
    target_path: Path = PATH_ASSETS / relative_path
    if not target_path.exists():
        if PROJECTS is None:
            return marimo.Html('<span style="color:orange">Can\'t access assets</span>')
        else:
            target_path.parent.mkdir(exist_ok=True)
            shutil.copy(PROJECTS / relative_path, target_path)
    extension = relative_path.split(".")[-1]
    assert extension == "pdf"
    if marimo.running_in_notebook():
        return marimo.pdf(target_path)
    return marimo.Html(f"<iframe src=/assets/{relative_path}>")
