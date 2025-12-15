
import marimo
app = marimo.App(width="medium")
@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "# The beginning")

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
# The beginning
""")

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
Ok, let's do this.
""")

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
This is my first note in what may become a long series of posts in on [My blog]([[Home]]) .
""")

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
I wanted to do that for a long time, but never actually committed. Now is the time.
""")

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
There are a few reasons why I decided to invest time into this seemingly needless project. Here are a few:
    - because I like to write
    - because I'm not that bad at writing
    - because I need to write
    - because [D.M](http://www.madore.org/~david/weblog/) is my hero
    - because not having a great reason to do a thing is not a great reason to not do the thing
    - to write better english
    - because if the habit sticks, my dopamine machinery will make this activity even more enjoyable than watching youtube
    - because people may actually learn a thing or two by reading my blog
    - because writing a rant about stuff you are frustrated about is the best way to make the frustration fade away
    - because I am lucky enough to have a computer, ten fingers, and a brain to do it
    - because the internet is currently being collapsing under a pile of AI slop, and #NoBullshit #NoAI #MadeByHuman stuff is becoming something precious. At least my near geek friends will appreciate that.
    - because I recently overcame a health issue that was slowly eating a large part of my life, and I want to celebrate it. I will certainly write something about it in the future.
    - because it's December ! Everyone is doing a king of advent calendar (whether it be chocolate, photos, advent of code ...). Too bad I did not start at 1th December though. But clearly late now is better than maybe on time later
""")

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
Don't expect anything. Or do, who am I to say you not to.
""")

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
That's all for today. Bye !
""")
