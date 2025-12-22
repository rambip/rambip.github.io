
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Rush", [])

    

@app.cell(hide_code=True)
def _():
    mo.md(rf"""
# Rush

Today was a short day of work. I had to be efficient to not lose time. No detail, no useless stuff. Just the core, just the code. I don't want to lose time. But keep control at the same time. Unstable balance.

8:30 to 12:00 -> work

12:00 to 12:30 -> cook

12:30 to 13:00 -> eat

13:00 to 16:00 -> work

After that, take a bag, a computer, and let's go. I'll visit my father's taunt. Chose a theme for today's blogpost. And write quick.

It's so hard to not backspace ! What if I make a mistake ? I promised I would try to write less typos. That takes times. Too much times.

But there is a pleasure in writing fast, in letting your brain go off rails, or perhaps stay on its own rails, jumping from an idea to another. I should do that more often. Writing with your unconscious self.

No regrets, don't look back. There is a monster behind you. The monster of wasting time. The monster of doubt. DON'T. LOOK. BACK.

Did I ever mention LLM-izing myself ? That's exactly what I'm doing. Follow the next token, let luck and a bit of intuition guide the process. I'm the chain of thought.

Maybe I should rename this page "writing without thinking" ? Or "unconscious rambling" ? Or Don't look back ? Nope. Don't edit that title, buddy.

You can't see the flow of time in my writing, that's pretty strange. When you say something at loud, timing is precious. This brings so much information about what you already knew and what you need to think about while talking. But here, no indication about the time between 2 words. If I take 2 minutes without a single idea, you can't know it. Maybe I should type the same character again and again when I don't have any mode idea ?

............................................................................................................................. ok got it

I remember that a friend told me about an horrible website (or a feature of some text editor, can't remember) that starts to delete what you write if you don't write fast enough. This way, there is no more doubt about how much time you spent writing a word. Each word has the same content of thought. No, each word has around the same content of reflexion, because your short term memory can queue idea while you are typing them.

Again, that's very similar to a LLM. Each token is pretty boring, you may need a lot to get a breakthrough............................................. I need a new idea right ?

I don't think I could start this sentence without a good idea because otherwise how would I start this sentence ? Wow that's magic. Really don't understand what's going on.

I really have to finish this dumb article about sandwiches, otherwise it will stay on my mind forever. I really appreciate that people read my website. I have no idea if my usual readers will appreciate this mess. Do I care ? Maybe.

Ok, time's up. Bye !
""")
