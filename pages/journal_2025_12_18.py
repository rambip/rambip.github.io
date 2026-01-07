
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Tong twisters", [])

    

@app.cell(hide_code=True)
def _():
    mo.md(rf"""
# Tong twisters

Tong twisters are so funny. I think I have even more fun creating them than reading them aloud. I'm better at it in french, I also create some English ones. Give them a go:
- The pill spills a papaya's peal
- Chuck's coach checked Chuck's couch and Chuck choked
- Monotone autumn's tone tons a ton, Tom
- A Dyadic's Dick addict
- Zibi the abyss busy bee buzz its busty besty
""")
