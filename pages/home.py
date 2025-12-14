import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from here import me
    return me, mo


@app.function(hide_code=True)
def home_page():
    from here import include
    return include(__file__, globals()["app"], "home", url="index.html")


@app.cell(hide_code=True)
def _(mo):
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
def _(mo):
    mo.md(r"""
    ## The stuff
    """)
    return


@app.cell
def _():
    import rubiks
    rubiks.page_()
    return


@app.cell
def _():
    import journals 
    journals.page_()
    return


@app.cell
def _():
    import ascii
    ascii.page_()
    return


@app.cell
def _():
    import love_typst
    love_typst.page_()
    return


@app.cell
def _():
    import academic 
    academic.page_()
    return


@app.cell
def _():
    import minimal_design
    minimal_design.page_()
    return


if __name__ == "__main__":
    app.run()
