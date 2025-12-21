
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Nonsense", [])

    

@app.cell(hide_code=True)
def _():
    mo.md(rf"""
# Nonsense

What is the difference ?

How would you explain time to someone who does not use it ?

Aren't you alright ?

How much wood would a woodchuck chuck if a woodchuck could chuck wood ? ([here](/journal_2025_12_18.py.html) for more)

Would you go barefoot if you were Gandhi, all else being equal ?

What is the exact size of a pine tree ?

What is yellow and may not be the answer to this question ?

Where am I ?

How is written the most used word in the universe ?

Do you like water ?
""")
