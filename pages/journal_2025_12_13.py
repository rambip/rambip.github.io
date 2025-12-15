
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# Sandwiches", [])

@app.cell(hide_code=True)
def _():
    mo.md(r"""
# Sandwiches
You know what a sandwich is right ? Stuff between 2 layers of bread, something like that.
I thought I knew what sandwiches were too. But it was before I encountered this monstruosity:
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/An_image_of_a_toast_sandwich%2C_shot_from_the_side.jpg/250px-An_image_of_a_toast_sandwich%2C_shot_from_the_side.jpg)
A [Toast Sandwich](https://en.wikipedia.org/wiki/Toast_sandwich). A fu\*ing **Toast Sandwich**. A piece of bread between 2 pieces of bread.
At this point in time, the entire universe collapsed around me. What even is a sandwich ? Is toast itself a sandwich ? Is a Toast Sandwich a Sandwich Sandwich ? If you stack 2 layers of bread one on top of the other, is it a Nothing Sandwich ? I'm becoming insane, this is clearly not a sandwich. We have to ban it for the name of sanity.
    - No, wait a second. It must be a sandwich 😨. And I think I can prove it
        - Axiom 1. We assume that if $X$ is a sandwich, $X$ with half as much filling is a sandwich. By induction, for any $n$, a sandwich with $2^{-n}$ as much filling is a sandwich.
        - Axiom 2. We assume that sandwiches exist. This is a non-obvious fact, but this implies that they are made of atoms. In particular, the filling is made up of a finite number of atoms.
        - Axiom 3. There is at least one person on earth that know what a sandwich is, and this person is not a scientist.
        - Axiom 4. A hamburger is a sandwich. This fact is trivial.
        - By 1) and 2), a sandwich with one atom of filling is a sandwich.
        - But then by 3), the person who knows what a sandwich is can't make the difference between this sandwich and a sandwich without filling. We just proved an important theorem: **a sandwich without filling is still a sandwich**
        - By 4, we know that this is a sandwich. Let's call it $S_3$:
            - ![](https://www.pngplay.com/wp-content/uploads/15/Mcdonalds-Big-Mac-Transparent-PNG.png)
        - By our previous theorem, a $S_3$ without feeling is a sandwich.
        - But this is equivalent (in a strong sense) to a Toast Sandwich.
    - > [Now I am become Death, the Destroyer of Worlds**](https://theconversation.com/now-i-am-become-death-the-destroyer-of-worlds-the-bhagavad-gita-explained-214365)
We have to do something then. We have to classify sandwiches once and for all.
# The State of Research
This research is one of the uttermost importance. Generations of researcher have debated on the subject, and we only start to see the premises of a universal classification.
⚠️ This can be a very emotional and polarizing subject, so beware.
    - ![](https://cuberule.com/assets/09_sandwich.jpg)
-
## Definitions
Before I present the main theories, we need some definitions.
    - *structural starch* is anything made up of long chains of mostly glucose, that can be hold in one hand
    - *bread* is a kind of structural starch. But **a** bread is very different.
    - What we will refer to as *salad* is anything that is edible and that is not structural starch. For example,
To make sure you understood, here are some basic questions:
    - <details>
          <summary>Is rice structural starch or salad ?</summary>
          Salad. You can't hold rice in your hands. The only exception is suchi, when rice becomes structural starch.
      </details>
    - <details>
          <summary>Is lettuce salad ?/summary>
          
      </details>
    - <details>
          <summary>What is a potato </summary>
          Here is the extra info you were looking for.
      </details>
""")
