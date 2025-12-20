
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Go hug a tree", [])

    

@app.cell(hide_code=True)
def _():
    mo.md(rf"""
# Go hug a tree

![](https://trackslesstravelled.com/wp-content/uploads/2022/11/Styx-Tall-Trees-Forest-Reserve-standing-big-tree-1080x1350.jpg)
    - credits: [Candace Elms-Smith on trackslesstravelled.com](https://trackslesstravelled.com/styx-tall-trees-tasmania/)

If you know me well, you know some of my routines can seem ... strange.

In this post, I want to talk about one of them: hugging trees.

Each Sunday, I try to run for about one hour. I try to run as much as possible in parks or in the forest. And mid-way in my run, I stop, go hug a tree for 5 min straight, and go back running. I love it. It feels great.

It's hard to explain why it's the case to someone who never did it. So here is my advice: stop reading, find the most nearby tree, hug it, and go on with your reading. This way, I won't lost my time trying to explain what can be experienced instead.

The first benefit of hugging a tree is the meditative part. By wrapping your arms around the trunk and doing nothing else, you stop thinking for some time. It's like boredom, except you do something — kind of. To be honest, this moment of nothingness in your brain will likely last for less than a minute, and then the flow of thoughts will go back. I try to counter that with a trick: not thinking about it. That's meditation 101: when you feel that your minds escapes, you gently pull it back — to the trunk in this case.

Then, there are the sensations. You smell the lichen, the trunk and the moss. You see a complex spectrum of colors from brown to green, with infinite nuances and fractal patterns. You feel the asperities of the wood, the softness of the soil. You taste this delicious mushroom that was .. Please don't do that. And it's interactive: as you increase your grip or let go, you feel the tension inside your chest.

Beyond the sensations, it's the whole atmosphere, the whole vibe that your brain absorbs like a sponge. The sounds around you make a big part of that. Cyclic patterns, a tiny bit of wind. The birds that chat, sing, scream and their voices echo. The deem lights around you, undulating like the see as the patterns of leaves changes.

At a personal level, watching towards the top of a tree invokes a sense of eternity. If I die tomorrow, the tree will be there for years. Unless destroyed, the forest will be there for hundred of years. And unless [humanity accidentally creates a grabby unaligned super artificial-intelligence that convert every atom of the solar system into robots](https://www.lesswrong.com/posts/F8sfrbPjCQj4KwJqn/the-sun-is-big-but-superintelligences-will-not-spare-earth-a)

Hugging a tree in the forest is certainly not magic, but it feels like it. Maybe the explanation is a lot simpler: we miss it. After millions of years of evolution, our brain and organs may have somewhere the hardcoded information that forests are good. They can protect you, they host many resources, they are a source of food for who can decipher the secrets of plants. In your average day, how many times do you see a tree ? For how long do you hear a bird ? How many times do you put your fingers in the soil, and do nothing but watch around you ? Your brain may be craving for this basic need or being embedded in this environment.

So think about it the next time you feel bad without knowing why. Go hug a tree, and enjoy a slice of eternity.
""")
