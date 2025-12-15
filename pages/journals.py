
import marimo
app = marimo.App(width="medium")
@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "My blogposts")

@app.cell
def _():
    import journal_2025_12_10
    journal_2025_12_10.page_()

@app.cell
def _():
    import journal_2025_12_11
    journal_2025_12_11.page_()

@app.cell
def _():
    import journal_2025_12_12
    journal_2025_12_12.page_()

@app.cell
def _():
    import journal_2025_12_13
    journal_2025_12_13.page_()

@app.cell
def _():
    import journal_2025_12_14
    journal_2025_12_14.page_()

@app.cell
def _():
    import journal_2025_12_15
    journal_2025_12_15.page_()
