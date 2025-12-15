import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    from here import asset

    return (asset,)


@app.function(hide_code=True)
def page_():
    from here import Embed

    return Embed(__file__, globals()["app"], "My essay on minimalist design")


@app.cell
def _(asset):
    asset("minimalist-design/booklet.pdf")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
