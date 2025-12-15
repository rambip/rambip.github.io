import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")

with app.setup(hide_code=True):
    def page_():
        from here import Embed

        return Embed(__file__, globals()["app"], "Me in the working world")


@app.cell
def _():
    import marimo as mo

    from here import asset
    return (asset,)


@app.cell
def _(asset):
    asset("career/cv_en.pdf")
    return


@app.cell
def _(asset):
    asset("career/anti-cv.pdf")
    return


if __name__ == "__main__":
    app.run()
