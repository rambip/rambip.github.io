
import marimo
app = marimo.App(width="medium")
@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "# Fix yourself, then the world")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
# Fix yourself, then the world
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
A few years ago, I discovered [Effective Altruism](https://www.effectivealtruism.org/). If you don't know it already, it's the project and community backed by a philanthropic foundation (Effective Ventures). Here is what their goal is, as presented in the associated webpage:
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
> Effective altruism is a project that aims to find the best ways to help others, and put them into practice. 
> It’s both a **research field**, which aims to identify the world’s most pressing problems and the best solutions to them, and a **practical community** that aims to use those findings to do good.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
I have always wanted to have a clear purpose in my life, a "raison d'être". I don't know exactly why, but this seems obvious to me. It's always a bit strange to talk about it, because I feel that I shouldn't have to justify thinking about the best way to do good. Instead, shouldn't it be people who **do not** think about helping others who should have to justify themselves? Anyway.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
The point is: I think I discovered the project too early. To be clear, most of the things I will say in the following are not criticism towards Effective Altruism (EA for short). It's quite the opposite. I think we need this project more than ever, and I still think I would like to be more involved in it in the future.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
I was probably around 15 when I discovered EA. I was charmed, and it became my default way to see problems in the world. What I did not realize was that at this time of my life, I had a lot of challenges to overcome myself. Instead of fixing these problems, I kept looking outwards.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
Of course, I noticed them. You can't ignore things such as depressive symptoms, eating disorders and health issues. But I was passive. I don't say it would have been easy to fix them (like many, I had a lot of pressure, mainly because of [Prepa](https://fr.wikipedia.org/wiki/Classe_pr%C3%A9paratoire)). But the paradox remains: during years, I thought about optimizing policies in the world to do more good, and I did not even try to fix my problems. With a step back, this seems silly. I think I thought it was helpful to thing about doing good (and it may have been) but I was mistaken about the impact I could have.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
Let's say I go back in time. I meet my past self, and present him/me with a choice. In the next 3 years, you/I can:
    - try to do good in the world. In 3 years you will have low motivation, you will still have health issues and you will struggle to create your community
    - invest everything in fixing your own problems. In 3 years you will have more motivation, more focus, and people will be inspired by your enthusiasm.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
Presented that way, I hope my past self would see it as a no-brainer. Hence "Fix yourself, then the world".
    - This has nothing to do with this [creepy music](https://www.youtube.com/watch?v=wYxs2wrWuFc)
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
This take can seem a bit scary. But it's a very general advice, and it's as relevant for smaller problems. Recently, I constructed a new habit. Every evening before going to bed, I list problems I had in my day. You could think it's counter-productive, but not at all ! When I'm in a bad mood, I just don't have the force to open the notebook to write in the list. And when I'm in a good mood, I'm very happy to have identified such easily avoidable problems ! It increases your reflexivity (the capacity to think about yourself and your own habits). It may depend on your character, but for me at least it's clearly beneficial. Some elements in this list you may relate to:
    - > I wanted to close my computer at 9 PM, but thanks to a bug I wanted to fix, I closed it at 11PM. I'm not as strict on no-screen time before bed as I would like to be.
    - > During the meal, I was not able to start a conversation with my colleague.
    - > I constantly forgot X, Y or Z.
    - > I have made no progress for the last 2 months regarding running, and I feel a bit weak.
    - > This key on my keyboard is stuck, I should really investigate why.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
The point is, listing the problems may be the hardest step in the process of becoming a better person. To list a problem, you need to become aware of it and to decide it's a problem. You immediately start to think about how to fix it. I found a brief discussion on this subject on [LessWrong](https://www.lesswrong.com/posts/gtk2KqEtedMi7ehxN?commentId=JiAevyygcifE3Whiw)
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
And once you fix the first one, you start the procedure. There is an entire mindset that I could call the "fixing mindset". It's the exact opposite of procrastination, and it's related to the [Growth mindset](https://en.wikipedia.org/wiki/Mindset#Fixed_and_growth_mindset). Once you fix the smaller problem, you have more "energy" — by lack of a better term — to tackle bigger ones. The easiest problems in the list are related to stuff (stuff to buy, stuff to repair, stuff to change). But as soon as you try to tackle harder problems, you will have to deal with the eternal monster: *your own habits*. There is now good-quality research about how to break and form new habits ([this](https://www.youtube.com/watch?v=HXuj7wAt7u8) may be a good introduction), and this is very often the same pattern.
    - 1) take the decision to change something in your life (smoking, drug, videogames, you name it)
    - 2) find a system to detect each time you have the unwanted behavior. Each time you detect it, note it (or do anything that makes you more aware of it). Look at what triggered it.
    - 3) each time you identify the trigger, try to deviate from the habit, and replace the action by something else.
    - 4) be completely free from the habit
    - 5) have more motivation to tackle another one.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
Of course, it's not easy. And it's not even always possible. People fail, people relapse, people need help. But if you are lucky enough to consider fixing some of your problems yourself, do it. If that sounds like personal development advice, it's because it is. That does not make it less valid.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
And if you're even more lucky, you have already fixed most of your problems. If that's the case, go help others fix theirs. That's what Effective Altruism is about, and that's wonderful.
""")

@app.cell(hide_code=True)
def _():
    mo.md(r"""
Have a nice day, but do not be blind to your problems.
""")
