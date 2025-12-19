
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Written by hand", [])

@app.cell(hide_code=True)
def _():
    mo.md(r"""
# Written by hand

![image.png](../assets/image_1766167930643_0.png)
""")
