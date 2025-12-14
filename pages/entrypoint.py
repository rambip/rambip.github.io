import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    from here import setup_everything
    return (setup_everything,)


@app.cell
def _(setup_everything):
    setup_everything()
    return


@app.cell
def _():
    from home import home_page
    home_page()
    return


if __name__ == "__main__":
    app.run()
