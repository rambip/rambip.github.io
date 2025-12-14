import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # [SVGBOB](https://ivanceras.github.io/svgbob/)
    """)
    return


@app.cell
def _():
    import marimo as mo
    import vye_svgbob
    from marimo import Html
    return Html, mo, vye_svgbob


@app.function(hide_code=True)
def page_():
    from here import include 
    return include(__file__, globals()["app"], "Ascii art")


@app.cell
def _(Html, vye_svgbob):
    ascii_art_1 = r"""
                                                                                 *
        0       3                          P *              Eye /         ^     /
         *-------*      +y                    \                +)          \   /  Reflection
      1 /|    2 /|       ^                     \                \           \ v
       *-+-----* |       |                v0    \       v3           --------*--------
       | |4    | |7      | ◄╮               *----\-----*
       | *-----|-*     ⤹ +-----> +x        /      v X   \          ,-.<--------        o
       |/      |/       / ⤴               /        o     \        ( / ) Refraction    / \
       *-------*       v                 /                \        `-'               /   \
      5       6      +z              v1 *------------------* v2    |                o-----o
                                                                   v
    """
    Html(vye_svgbob.to_svg(ascii_art_1))
    return


@app.cell
def _(Html, vye_svgbob):
    ascii_art_2 = """




                        V                                                     Y        
                                                                     X    ┌──────-──┐   
            ┌──────────────────-───┐                         ┌────────────┼───┐     │   
            │                      |                         │            │   │     │   
                                                                                    │   
    ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌─-─┐                ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌─-─┐ 
    │ A │  │ B │  │ C │  │ D │  │ E │                │ A │  │ B │  │ C │  │ D │  │ E │ 
    └───┘  └───┘  └───┘  └───┘  └───┘                └───┘  └───┘  └───┘  └───┘  └───┘ 

    │                        │                       │                        │        
    └────────────────────────┘                       └────────────────────────┘        

                U                                                U                                                            
    """                                                                                         
    Html(vye_svgbob.to_svg(ascii_art_2))
    return


if __name__ == "__main__":
    app.run()
