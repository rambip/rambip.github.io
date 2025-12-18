
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# La Louve", [])

@app.cell(hide_code=True)
def _():
    mo.md(r"""
# La Louve

I've been very busy today. Not only did I work all day on restructuring and making future-proof an embedding based survey answer analysis algorithm (with cool visualisations and a  bit of LLMs on top) — more on that in a future day — , I spend all my evening in a super cool, but time-consuming place. As a result, it's 23:30, I'm still running on adrenaline, and I'm writing this shitty blogpost because I hope to keep up the pace. Hopeful, I will be able to rest a lot during my winter holidays (I hope it's True).

What's this place you may ask ? It's called *La Louve*. *La Louve* is a both a community of 5000 persons, a cooperative, and a supermarket. Here is how it works in a nutshell:
    - To be a member of *La Louve*, you buy a part of the cooperative, you become [actionnaire].
    - You gain the right to do your groceries at the supermarket *La Louve*, with very healthy items and at a very low price
    - You also sign a contract which makes you a sort of "forced volonteer". Once every 4 weeks, you have to do a 3 hour service. Compared to how much money you save when you do your groceries, it's clearly worth it.

Today was my second service. But there was a problem: I never had time to do the **strongly advised** in-depth visit of the building. And the only opportunity this week was just after my service. So 16:15 -> 19:15 = adding beverage and juices to the [rayons], 19:15 -> 19:35 = bying stuff, 19h:35 -> 21:10 was the visit, 21:30 -> 22:30 was eating, and I still had some things to check on my computer, so 23:00 -> 00:00 = finding a way back home through Paris' Subway.

But seeing how a supermarket works is really interesting ! The logistic is insane, and you see how an error during the [livraison] impacts the entire chain, and can cause problem at client checkout. It's crazy how much effort goes into unpacking, repacking, distributing, dumping, cleaning, uncleaning and re-cleaning again, packing the packaging, dumping the packaging packs, cleaning the packaging-packing machines ... And coordinating all these steps. But when you think about it, you just have to. Unless each individual has a cave and a gigantic fridge, products that can't go out of date, a truck to get food every few months, and a lot of containers of various sizes: in this case, you don't need any supermarkets.

Still, I think the current model of enormous, plastic-addicted, 100% capitalist stuff-storing halls can be greatly improved. And *La Louve* is, above all else, a very useful experiment to do what can be done differently, and what can't (or at least can't yet).
""")
