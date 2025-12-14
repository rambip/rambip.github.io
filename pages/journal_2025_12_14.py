
import marimo
app = marimo.App(width="medium")
@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "-")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
-
-
""")
