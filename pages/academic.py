import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import shutil
    from here import asset
    return (asset,)


@app.function
def page_():
    from here import include 
    return include(__file__, globals()["app"], "Me in the working world")


@app.cell
def _(asset):
    asset("career/cv_en.pdf")
    return


@app.cell
def _(asset):
    asset("career/anti-cv.pdf")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
