from pathlib import Path

PATH_PAGES = Path(__file__).parent / "pages"

CELL_TEMPLATE_MD = """
@app.cell(hide_code=True)
def _():
    mo.md(r\"\"\"
{md}
\"\"\")
"""


INIT_EXPORT = """
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    {imports}
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "{description}", [{children}])
"""

IMPORT = """
@app.cell
def _():
    {name}.page_()
"""


def main():
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
                content = (
                    content.replace("\n  ", "\n")
                    .replace("\t", "    ")
                    .replace("\n- ", "\n\n")
                )

                f2.write(INIT_EXPORT.format(description=title, imports="", children=""))
                f2.write(CELL_TEMPLATE_MD.format(md=content))
        with open(PATH_PAGES / "journals.py", "w") as f:
            imports = "\n    ".join(f"import {name}" for name in names)
            children = ",".join(f"{name}.page_()" for name in names)
            f.write(
                INIT_EXPORT.format(
                    description="My blogposts", imports=imports, children=children
                )
            )
            for name in names:
                f.write(IMPORT.format(name=name))


if __name__ == "__main__":
    main()
