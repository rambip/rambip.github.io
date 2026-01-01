
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Me and AI, a short summary", [])

    

@app.cell(hide_code=True)
def _():
    mo.md(rf"""
# Me and AI, a short summary

I always have been interested by the way algorithms are used to share information, and how it impacts the world (politics, learning, wellbeing ...). I slowly started to read about Stuart Russel, Yudkowski and french authors such as Lê Nguen Hoang, but without taking them too seriously.
When I turned 20, I realized that the "AI" curriculum of the prestigious university I was in was complete trash: no mention of AI risks, heavy focus on the environment even when it's not relevant, courses about machine learning stuck in the 80s ...
So I figured I would learn about AI safety on my own, and even create my community to raise awareness around me. It was the only way for me to find a meaningful goal in my life, but the idea of a Super Intelligence that would disrupt the entire political / economical / biological system seemed really abstract and far away.
After a conversation with a friend, I was forced to admit that the possibility of ASI was terrifying, and that I had to take it more seriously. At this moment, I was talking regularly with people from the french AI safety center. I also met Maxime Fournes at this moment, and I found his discourse to be extremely clear and to the point.

I had a hard time dealing with the crazy thought. But like any other crazy scary thought, weelbeing, mindfulness and psychological exercices help you overcome them.
Now, I still think we may be cooked, but I don't feel bad about it. If it's the natural and logical way our species go extinct, well ok. But at the same time, I do my best to invest my energy in what might save us (pauseIA, interpretability research, convincing young and talented people who will work in AI).
-

https://docs.google.com/forms/d/e/1FAIpQLSc9kB3MgloJ0D2oMeNxBwKnnWnXwqajnEnvGJQaueug75_WcQ/viewform
""")
