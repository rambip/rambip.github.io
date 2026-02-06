import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")

with app.setup(hide_code=True):
    from pathlib import Path
    from jinja2 import Environment, FileSystemLoader

    import academic
    import ascii
    import digestion
    import journals
    import lambda_calc
    import love_typst
    import marimo as mo
    import minimal_design
    import rubiks

    from here import Embed, PATH_MARKUP

    # Setup Jinja2 environment
    jinja_env = Environment(loader=FileSystemLoader(PATH_MARKUP))
    template = jinja_env.get_template("template.jinja")

    def page_():
        return Embed(
            __file__,
            globals()["app"],
            "Rambip's website",
            [
                ascii.page_(),
                rubiks.page_(),
                love_typst.page_(),
                journals.page_(),
                minimal_design.page_(),
                academic.page_(),
                lambda_calc.page_(),
                digestion.page_(),
            ],
            url="index.html",
        )

    def generate_website():
        dest = Path(__file__).parent.parent / "web"
        dest.mkdir(exist_ok=True)
        root = page_()

        # Render all children with standard template (not home)
        for state in root._execute_children():
            html_content = template.render(
                title=state.title,
                name=state.path_name,
                content=state.content,
                home_page_url="/index.html",
                is_home=False,
                python_content_encoded=state.python_content_encoded,
                python_filename=state.path_name,
                python_content_for_marimo=state.python_content_for_marimo,
            )
            with open(dest / state.url, "w") as f:
                f.write(html_content)

        # Render home page with is_home=True
        home_state = root._execute_notebook(root.python_content, hash(root))
        html_content = template.render(
            title=home_state.title,
            name=home_state.path_name,
            content=home_state.content,
            home_page_url="/index.html",
            is_home=True,
            python_content_encoded=home_state.python_content_encoded,
            python_filename=home_state.path_name,
            python_content_for_marimo=home_state.python_content_for_marimo,
        )
        with open(dest / home_state.url, "w") as f:
            f.write(html_content)


@app.cell
def _():
    IN_THE_MATRIX = False
    return (IN_THE_MATRIX,)


@app.cell
def _():
    from here import me

    return (me,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Antonin's Website

    Hey ! It's me, Antonin @rambip

    As you probably notice, this is not a very usual website. But I bet you will love it !
    """)
    return


@app.cell
def _(me):
    rambip = me()
    rambip
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## The stuff
    """)
    return


@app.cell
def _():
    journals.page_()
    return


@app.cell
def _():
    rubiks.page_()
    return


@app.cell
def _():
    ascii.page_()
    return


@app.cell
def _():
    lambda_calc.page_()
    return


@app.cell
def _():
    love_typst.page_()
    return


@app.cell
def _():
    academic.page_()
    return


@app.cell
def _():
    minimal_design.page_()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # The secret sauce
    """)
    return


@app.cell
def _(IN_THE_MATRIX):
    if not mo.running_in_notebook() and not IN_THE_MATRIX:
        generate_website()
    return


if __name__ == "__main__":
    app.run()
