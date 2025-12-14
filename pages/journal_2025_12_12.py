
import marimo
app = marimo.App(width="medium")
@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "# Bullet points")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
# Bullet points
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
If you read the previous entries in my journal / blog post / thought dumping substrate, you probably noticed the way of writing is special.
id:: 693c7d29-1968-4ae4-97d4-8f6ddf35e0fe
    - It's probably not related to style, but to formatting
    - You may find it very annoying
        - maybe even clunky to read
    - And you're probably wondering when the next item in this list will be.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
This is a semi-deliberate choice. I decided to give a go to [LogSeq](https://logseq.com/), a note-taking #OpenSource software that is built around the idea of "blocks". This mean that every content, every conceptual knowledge item is an item in a list. This allow to do funny things like linking to [other blocks](((693c7d29-1968-4ae4-97d4-8f6ddf35e0fe))). That's completely overkill for a blog, and probably pointless. But I had to try to be sure. And [adding constraints](https://oulipo.net/fr/oulipiens/o) drives progress.
    - As a side note, I implemented part of the blog generation logic by myself. So they are missing features, and I'm not sure I will have the time / motivation to implement linking blocks. I will probably write a post about how this blog generator works in the future.
      id:: 693c81cf-36f5-484e-a37a-881806f52a7c
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
So let's list some **advantages** of list items
    - They are easy to display with html
    - They can be nested recursively
        - They can be nested recursively
            - They can be nested recursively as deep as you want
                - They can be .. ok I think you got the point
    - Because they are trees, they can represent a wide variety of data:
        - [Dendograms](https://en.wikipedia.org/wiki/Dendrogram)
        - Typologies (classes and subclasses)
        - folders
        - very detailed tasklists
    - They force you to thing about structure first, content second
    - they are faster to type, and I have also noticed that they are easier to write than paragraphs when I'm brain-dead
        - talking about [being brain dead](https://www.oulipo.net/fr/99-notes-preparatoires-aux-99-notes-preparatoires) ...
    - They can be folded, which is [very powerful for explanations](https://ncase.me/nutshell/)
    - They reflect the [Dyck language](https://en.wikipedia.org/wiki/Dyck_language). Make what you want from this information.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
And some **drawbacks**:
    - Tree are less expressive than graphs
        - They can't handle cycles
        - They can't handle repeating repeating content, see ((693c81cf-36f5-484e-a37a-881806f52a7c))
        - They are directed. You can't have just 2 blocks that refer to each other like [wikipedia pages](https://en.wikipedia.org/wiki/Wikipedia:Walled_garden)
    - They can get very boring. If you sleepwalk into them. They kill narration and remove emotion. Here is an illustration:
        - List items can be boring
        - In particular when they repeat
        - In particular when they repeat
        - When there is no connection
        - When sentences are the same
        - When there is no rythm
        - They are boring as fuck
        - You may need [this remedy](https://wooorm.com/write-music/)
    - LLM love them. So you may LLMize yourself
        - I jailbroke myself LOL
        - Wait, actually it is not what the user want. Let's re-think about the situation
        - In conclusion, list items have advantages and drawbacks — You have to chose wisely when they should be used.
            - https://kieranhealy.org/files/papers/fuck-nuance.pdf
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
Ok, I think I will stop there.
    - Well, technically, you added a line after that 🧠
        - Shut up !
""")
