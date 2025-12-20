
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Sick sucks", [])

    

@app.cell(hide_code=True)
def _():
    mo.md(rf"""
# Sick sucks

I'm sick. It sucks.

I feel dizzy, my mind's fuzzy.

This night was so long, remember every minute of it. Sort of continuous hallucinations, I'm stuck in a loop of thoughts, My brain's of rails.

Too much adrenaline the last few days, might be the comedown.

My nose's clogged, my throat's melted, my ears' glued.

HEADACHE. diiiaaarrhhheaaa

Hot and cold together, I feel torn, what a hell

But no fever, no soreness. What's going on ?

Doing nothing seems undoable. But doing something sound even worth.

My bed is my  poisonous cocoon and my great prison.
""")
