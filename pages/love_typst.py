import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import typst as typst_lib
    import marimo as mo
    return mo, typst_lib


@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "The greatest markup language")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I 💖 [typst](https://typst.app/)
    """)
    return


@app.cell
def _(mo, typst_lib):
    header = """
    #set page(width: auto, height: auto, margin: 10pt)
    #set text(size: 20pt)
    """
    def typst(input):
        source = (header + input).encode("utf-8")
        svg = typst_lib.compile(source, format="svg")
        return mo.Html(svg.decode("utf-8"))
    return (typst,)


@app.cell
def _(typst):
    typst("$(oo -> oo) / (1 eq 1)$")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
