
import marimo
app = marimo.App(width="medium")
with app.setup(hide_code=True):
    import marimo as mo
    
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "# My new year Theme", [])

    

@app.cell(hide_code=True)
def _():
    mo.md(rf"""
# My new year Theme

I remember a video from a few years ago, that was really influential for me. It was [Your Theme](https://www.themesystem.com/) from CGP-grey. I think this video was the first time I realized that there is a huge difference between intent and action. Here is a way to think about it:
- The first order approximation of a Human Being is a [sphere](https://en.wikipedia.org/wiki/Spherical_cow)
- The second order approximation of a Human Being is an agent with goals (or intents), resources to reach these goals, and external constraints.
- And if you want a more precise approximation, you have to take into account internal constrains. You have to admit that Human behavior is not driven solely by goals, but also (and most importantly) by psychological processes.

The moment I watched this video, I started to think that humans are not agents with goals. In particular, **I** am not an agent with goals. I still had a very bad model of human psychology and physiology, but at least I looked beyond the second approximation. For those who do not want to see the video, here is a `TL;DR`:
- > There are both empirical and theoretical reasons to think that new year Resolutions are counter-productive, or at least a missed opportunity. Resolutions are not flexible, in the sense that you may give them up because you realize they do not provide the benefits you thought. They are not inspiring, because it focuses on doing more X, when you think X is hard. And they do not help to make decisions in your life: most changes in your life imply giving up on some things, and framing your goal as a Resolution ignores this aspect. A better approach is to chose a new year **Theme** you will follow this year.

Even if I think that this video was a pivotal moment for me, I am quite critical of this idea of a **Theme**. Of course, it's way better than a new year Resolution, but it can't be a basis to build on.
- Let's go back to the idea of approximations of a Human Being. My third order approximation of a human being is a "Habit machine with a compass". In your brain, there is a machinery dedicated to forming, adapting and following habits. It's a [very old and core area](https://scientificpsychology.in/basal-ganglia/) of your brain, and it explains a lot of how you function as a person. On top of this machine habit, there is a compass encompassing (lol) your values, goals and emotions.
- If you chose a new year Theme without understanding the "Habit machine" part, you will likely fail. Start by [Fixing yourself]([[Dec 14th, 2025]]): your health, your destructive habits, your shitty situation. A new year resolution (or a new year theme, for that matter) is a very bad tool for this job. In my mind, the Theme is the cherry on top of a [Development Sytem](https://www.lesswrong.com/posts/mpbtk2xBjqjL7p5uQ/personal-development-system-winning-repeatedly-and-growing), in no way its basis.
- If you have a solid Development System, and healthy habits, a Theme becomes useful. It helps you make hard decisions when you have to chose between two conflicting values. Caring about oneself of caring about the others ? Sport or culture ? Achievements of Family ?

But since I have made quite a lot of progress on my Development System, and that I am increasingly happy with my habits, choosing a Theme makes sense. And without further suspense, here it is:
- <details><summary>my Theme for 2026 is ...</summary><h3><i>Finishing my projects.</i></h3></details>

That's right. Not very sexy or inspiring, I know. But that's what I want to focus on.

There are a few reasons why it seems the right time to focus on this theme:
- I have a lot of unfinished projects. I mean a lot. On my computer, I have a `Project` directory, and I created one folder for every project I have worked on. I have 206 folders. Most of them are done and I will never work on them again, but they deserve a decent end, with an explicit "this project is done" mention.
- It's very satisfying to remember the process of making a thing from start to finish. In my family, the person who cares the most about finalizing is my father. When he makes something in the house (let's say the electrical box), he always spends a significant amount of time polishing the result and making sure it's pretty and pleasant to use. And at the end of the day, it sure feels like something to be proud of.
- It's easier that starting new projects. When something does not work, you can switch to another one to not feel stuck in a dead end. Of course, you have to come back to the first project, otherwise you're defeating the entire concept of finishing projects.
- It can be a starter to gain motivation for new projects. Finishing a project has the same effect as checking an item in a TODO-list.
- Unfinished projects are a pity on a CV.

In practice, I already foresee upcoming challenges:
- It will be time-consuming. And it will obviously go slower than I expect, because most of the time a project is left unfinished is because it goes too slowly or it's too hard.
- For some projects, you have to decide what "finishing" is. You can try to define in advance what will be the "state of completion" of the project, but it will probably evolve until you reach this point.
- Perfectionism is self-defeating. I a project starts to consume too much time, I will have to finish it even if I know I could theoretically do better.
- I need to prioritize. Some of my projects are 90% complete, but some of them are 10% complete. I can't take them at random.
- Finishing projects tends to be boring, starting new one tends to be thrilling. Some days, I will have a demon on my shoulder whispering: "go create this proof of concept, it will be so fun ! And don't worry, it will be very fast ..."

But I feel motivated to do it. Here are some projects you can expect me to complete (and for some of them, published on my website) in the next few months:
- A blog article explaining this f***ing health problem I recently overcome and never actually wrote about
- My blog article on an universal theory of sandwich classification ([[Dec 13th, 2025]]) finally completed
- An interactive explainer on lambda-calculus
- A breakdown of an algorithm I created at work, for automatic survey answers analysis
- Writing my second "AI Safety" Poem
- Finally having my full split and my "[Traction enroulée]({{{{video https://www.youtube.com/watch?v=slL4BO1Rs5U}}}})" (sorry, I think this concept simply does not translate to english)
- Running 10km under 50min
- and a lot of other stuff.
- (PS: also I plan to write English with less syntactical and grammatical errors, but it's hard to see what the completion of this project will be)

So to wrap it up: fix yourself, find a theme for your psychological compass, and have fun surviving 2026 ! Cheers.
""")
