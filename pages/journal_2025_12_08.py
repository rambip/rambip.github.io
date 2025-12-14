
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo

@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "")

@app.cell(hide_code=True)
def _():
    mo.md(r"""

""")
