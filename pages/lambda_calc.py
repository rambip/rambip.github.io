# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "curryparty==0.4.0",
#     "marimo>=0.19.7",
#     "polars==1.38.0",
# ]
# ///

import marimo

__generated_with = "0.19.7"
app = marimo.App(
    width="full",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)

with app.setup(hide_code=True):

    def page_():
        from here import Embed

        return Embed(
            __file__, globals()["app"], "Curryparty: a pinch of Lambda Calculus"
        )


@app.cell
def _():
    import marimo as mo
    import polars as pl
    from curryparty import L, o

    return L, mo, o


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <p align="center">
      <img src="https://github.com/rambip/curryparty/blob/main/logo.svg?raw=true" width="500px"/>
    </p>

    # Curryparty: a pinch of Lambda calculus

    You're tired of Turing Machines ?

    Your functionnal programming friends make fun of you because you don't know what a $\beta$-reduction is ?

    You think "currying" describes the action of adding spices to your dishes ?

    Then, you *absolutely* need to learn the basics of Lambda ($\lambda$)-Calculus

    ## What is this ?

    This is a personnal project I created from scratch, to fulfil the very specific mission of teaching lambda-calculus in an interactive, visual way.

    The source code of the project is freely available on github, feel free to give me a star: https://github.com/rambip/curryparty

    Come with me, we're going on an adventure !

    ## Prerequisites

    1) To appreciate this journey into the world of pure functions, you need to have some prior knowledge of what a function is, or at least can do.

    I don't have a great resource for that. If you don't know what a function is, go learn some python
    - (or any programming language of your choice that is at least 5 character long. That's a good rule of thumb to avoid imperative and overcomplex languages: C, C++, Java, Rust)

    2) You also need to have a sense of what "Computability" is. This can be a very alien concept if you did not study Computer Science, and I think it gives a good motivation to understand $\lambda$-Calculus. As a teaser, I strongly recommend either:
    - reading the [**Church Turing thesis** article in Standford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/church-turing/)
    - watching this video on [The boundaries of comuptation](https://www.youtube.com/watch?v=kmAc1nDizu0)

    ---

    Now that you're introduced to the subject, let's go !
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # A world of functions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start with some rules:
    1. you can only `print(0)` or `print(1)` in your code. That's the only way you have to communicate with the external world.
    2. No loop, no if / then / else
    3. No operation (addition, substraction, logical operations ...)
    4. You can use functions.

    What do you think you can do with these rules ? Not much ? Let's see ...
    """)
    return


@app.cell
def _():
    print(0, end="")
    print(1, end="")

    # Not very interesting ...
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Challenge 0

    Print `0011` with maximum 2 `print` statements, and without ever "dropping".

    "Dropping" means either:
    - not returning a value from a function
    - calling a function and not using the return value

    For example:

    ```python
    def print_one_drop():
        print(1)
        # I did not return: I dropped

    ```

    Or:
    ```
    def print_one():
        print(1):
        return True

    print_one() # oh no, I dropped !
    print_one()

    ```

    <details>
        <summary>
            Solution
        </summary>
    ```py
    def o(x):
        print(0, end='')
        return x

    def i(x):
        print(1, end='')
        return x

    i(i(o(o(None))))
    ```
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This trick can seem strange, but you can do quite powerful things with it.

    If you combine the first trick with a second one (passing functions as arguments), you get this:
    """)
    return


@app.cell
def _():
    def p0(x):
        print(0, end="")
        return x

    def p1(x):
        print(1, end="")
        return x

    # second trick: pass functions instead of values
    def print_four_times(f):
        f(f(f(f(None))))

    print_four_times(p0)
    return p0, p1


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Challenge 1

    Write a function `boo` that print either `0` or `1`, depending on the argument. Remember, no "if" and no arithmetic !

    <details>
        <summary>
            Solution
        </summary>
    ```py
    def true(a, b):
        # left argument
        return a

    def false(a, b):
        # right argument
        return b

    def boo(side):
        return side(i, o)(None)

    boo(false) # print 1
    boo(true) # print 0
    ```
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We could have called these functions `left` and `right`. So why did I call these functions `true` and `false` ?

    There is a good reason for that. Look at this mind-bending magic:
    """)
    return


@app.cell
def _(p0, p1):
    def true(a, b):
        return a

    def false(a, b):
        return b

    def boo(side):
        return side(p0, p1)(None)

    def logical_not(x):
        return x(false, true)

    boo(logical_not(false))
    boo(logical_not(true))
    return boo, false, true


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Challenge 2

    Write a `logical_or` and a `logical_and` using the same structure as above.


    <details>
    <summary>
        Solution
    </summary>
    ```py
    def logical_or(a, b):
        return a(a, b)

    def logical_and(a, b):
        return b(a, b)
    ```

    </details>
    """)
    return


@app.cell(hide_code=True)
def _():
    def logical_or(a, b):
        return a(a, b)

    def logical_and(a, b):
        return b(a, b)

    return logical_and, logical_or


@app.cell
def _(boo, false, logical_and, logical_or, true):
    boo(logical_or(false, false))
    boo(logical_or(false, true))
    boo(logical_or(true, false))
    boo(logical_or(true, true))
    print()
    boo(logical_and(false, false))
    boo(logical_and(false, true))
    boo(logical_and(true, false))
    boo(logical_and(true, true))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Challenge 3

    The `church number functions` are defined in this way:

    ```py
    def one(f, x):
        return f(x)

    def two(f, x):
        return f(f(x))

    def three(f, x):
        return f(f(f(x)))

    ...
    ```

    Write a function `product(a, b)` that takes as input two "church number functions" and print as many ones as the product of a and b.

    Hint: you can use this function:
    ```py
    def print_n_zeros(n):
        def result(x):
            return n(o, x)
        return result
    ```

    <details>
        <summary>
            Solution
        </summary>
    ```py
    def four(f, x):
        return f(f(f(f(x))))

    def five(f, x):
        return f(f(f(f(f(x)))))

    def print_n_zeros(n):
        def result(x):
            return n(o, x)

        return result

    def mult(a, b, x):
        return a(print_n_zeros(b), x)

    mult(four, five, None)
    # result: 00000000000000000000
    ```
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    If you're not used to functionnal programming, you may have noticed something strange in the "print_n_zeros" function:
    ```py
    def print_n_zeros(n):
        def result(x):
            return n(o, x)
        return result
    ```

    We created a function on the fly, used some of the current context inside it (in this case, the variable `n`), and returned it immediatly. We gave it a name, but this name is completely arbitrary. We could have written it like this:

    ```py
    def print_n_zeros(n):
        return lambda x: n(o, x)
    ```

    What is this "lambda" keyword doing here ? Well, it allows to do exactly what we wanted: to create a function on the fly and to return it immediatly. That's the core idea of Lambda-calculus.

    I hope you start to have a an intuition of what lambda functions are, and what they allow to do.

    The next step is to define more formaly what these "lambdas" are.

    Personnaly, the first time I learned about lambda calculus was in this video from Computerphile. Highly recommend it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe(
        """
    <iframe width="560" height="315" src="https://www.youtube.com/embed/eis11j_iGMs?si=pa1AU6_5ICMOHAP8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Terms, lambdas and applications
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What we call a "Lambda-function" or $\lambda$-function, is a mathematical description of the functions we played with in the last part.

    A lambda-function is "something with variables" that "return something".

    Let's create one:
    """)
    return


@app.cell
def _(L):
    L("x").o("x").build()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here is how to read it:
    - the blue block means "take a value"
    - the gray line means "pass the value"
    - the red block means "returns the value"

    So what we created is the simplest possible lambda function: a machine that takes `x` and returns `x`.

    In python, this would be:
    ```py
    def _lambda(x):
        return x
    ```


    But a lambda can have multiple variables:
    """)
    return


@app.cell
def _(L, mo):
    return_first = L("x", "y", "z").o("x").build()
    return_second = L("x", "y", "z").o("y").build()
    return_third = L("x", "y", "z").o("z").build()
    mo.hstack([return_first, return_second, return_third])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's focus on the first diagram.

    It has multiple blue blocks, which means we take multiple things. To track them, let's give them names:
    - the first blue block (from the top) takes `x`
    - the second blue block takes `y`
    - the third blue block takes `z`

    The red block still means "return the value". But wich one ? To know that, we have to look at the gray line.

    Since the gray line connects the first blue block with the red block, that means it returns the first value, `x`

    From top to bottom, these functions are:
    ```py
    lambda x, y, z: x
    lambda x, y, z: y
    lambda x, y, z: z
    ```

    But there is another way to think about the machines we created. Let's focus on the last one. It's like a machine that takes x, and returns a new machine. This machines takes y, and returns yet another machine. Thist last machine takes z, and return z.

    You may find it confusing to think about the lambda-functions we created in this way, but it's worth it. You can see the exact same phenomenon in python:

    ```py
    def add(a, b):
        return a+b

    def add_curried(a):
        def add_to_a(b):
            return a+b
        return add_to_a

    # or equivalently
    def add_curried(a):
        return lambda b: a + b


    add_curried(3)(4)
    ```

    This process of transforming a function with 2 arguments into a function that *returns* a new function has a name. It's called **Curryfication** (in honor or [Haskell Curry](https://en.wikipedia.org/wiki/Haskell_Curry), another big name in the world of lambda-calculus)

    So we can take stuff and return stuff. We can't do much yet. We're missing something: **applying** (or *calling*) functions. Let's see that in action:
    """)
    return


@app.cell
def _(L):
    L("x", "f").o("f", "x").build()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's unpack it.

    This lambda function takes a value `x` (first blue block), then a function `f` (second blue bock), use the function `f` (left gray line) and pass the `x` value (right gray line) to it (black horizontal line).

    For readability, the function that is called is under a black dot, and with a yello border.

    That's it ! With these 3 ingredients (blocks that take arguments, blocks that return arguments, block that apply functinos), we can make any function we want. Before we go on, some terminology:
    - a "**Lambda**", or $\lambda$ , is a blue block. It corresponds to a single variable.
    - a "**Variable**" is a red block. It is "bound" to a specific lambda, indicated by a gray line
    - an "**Application**" is a horizontal black line. The function is the stuff inside the yellow border and the argument is at its right.
    - a "**Term**" is any combination of the above. If the thing at the top is a **Lambda**, it's called a lambda-function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's define the $\lambda$-terms we already saw in the python challenges:
    """)
    return


@app.cell
def _(L):
    do_nothing = L("x").o("x").build()
    do_nothing  # it's also called the "identity" function
    return


@app.cell
def _(L):
    l_false = L("a", "b").o("a").build()  # takes the left (first) argument
    l_true = L("a", "b").o("b").build()  # takes the right (second) argument
    l_false
    return l_false, l_true


@app.cell
def _(l_true):
    l_true
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Remember the "Church" functions from the python challenges ? The concept comes from $\lambda$-calculus, they are often called "Church numerals" ([Church](https://en.wikipedia.org/wiki/Alonzo_Church) was the main creator of $\lambda$-calculus).

    As a reminder:
    ```py
    zero = lambda f, x: x
    one = lambda f, x: f(x)
    two = lambda f, x: f(f(x))
    ...
    ```

    Look at the graphical representation below (use arrows to navigate). It's the same structure each time:
    - take `f` (blue block)
    - take `x` (blue block)
    - pass `x` through the function `f` a given number of time.
    """)
    return


@app.cell
def _(L, mo, o):
    zero = L("f", "x").o("x").build()
    one = L("f", "x").o("f", "x").build()
    two = L("f", "x").o("f", o("f", "x")).build()
    three = L("f", "x").o("f", o("f", o("f", "x"))).build()
    four = L("f", "x").o("f", o("f", o("f", o("f", "x")))).build()
    mo.hstack([zero, one, two, three])
    return four, one, three, two, zero


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's try something harder.
    """)
    return


@app.cell
def _(L, o):
    s_myst = L("n", "m", "f", "x").o("n", o("m", "f"), "x").build()
    s_myst
    return (s_myst,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This starts to look a bit abstract, but with a bit of practice, these diagrams can be read pretty easily. As an exercise, let's write the corresponding python function, just by looking at the diagram.

    The first step is to create 4 lambdas:
    ```py
    mysterious_function = lambda x1: lambda x2: lambda x3: lambda x4: ...
    ```

    Then, the rule of thum is: **read bottom to top**.

    By looking at the 2 red squares at the right of the last line, we see that `x2` is called with the argument `x3`. Then, `x1` is called on the result. Let's call the expression $\alpha = x_1(x_2(x_3))$

    ```py
    mysterious_function = lambda x1: lambda x2: lambda x3: lambda x4: ... x1((x2(x3))) ...
    ```

    The last step is to call $\alpha$ with the argument `x4`. That is what the yellow border without a background means.

    ```
    mysterious_function = lambda x1: lambda x2: lambda x3: lambda x4: x1((x2(x3)))(x4)
    ```

    In a textbook, this function would be written as:

    $\lambda x_1. \lambda x_2 . \lambda x_3 . \lambda x_4 . \quad x_1 (x_2 \; x_3) x_4$

    Exact same idea, except we place parenthesis differently for readability.


    ## Aside: composing and forwaring

    If we take a step back, we see that they are 2 ways to assemble a sequence of variables: _composing_ and _forwarding_.

    In python, you can think about them this way:
    ```py
    def compose(a, b, c, d, e, x):
        return a(b(c(d(e(x)))))

    def forward(a, b, d, e, x):
        return a(b, c, d, e, x)
    ```

    Below is an illustration. The "Application" nodes are represented with the $\circ$ symbol.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    style = """
    style f stroke:#ff3333, stroke-width:3px
    style g stroke:#ff3333, stroke-width:3px
    style h stroke:#ff3333, stroke-width:3px
    style x stroke:#ff3333, stroke-width:3px
    style app1 stroke:#ffcc00,stroke-width:3px
    style app2 stroke:#ffcc00,stroke-width:3px
    style app3 stroke:#ffcc00,stroke-width:3px
    """

    mo.hstack(
        [
            mo.vstack(
                [
                    mo.md("### Composition"),
                    mo.mermaid(f"""
        graph BT
        h[h] --> app1[⭕]
        x[x] --> app1
        app1 --> fx["h(x)"]

        g[g] --> app2[⭕]
        fx --> app2
        app2 --> gfx["g(h(x))"]

        f[f] --> app3[⭕]
        gfx --> app3
        app3 --> hgfx["f(g(h(x)))"]

        {style}


        """),
                ]
            ),
            mo.vstack(
                [
                    mo.md("### Forwarding"),
                    mo.mermaid(f"""
       graph BT
        f[f] --> app1[⭕]
        g[g] --> app1
        app1 --> fg["(f g)"]

        fg --> app2[⭕]
        h[h] --> app2
        app2 --> fgh["((f g) h)"]

        fgh --> app3[⭕]
        x[x] --> app3
        app3 --> fghx["(((f g) h) x)"]

        {style}
        """),
                ]
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now in our lambda calculus block representation:
    """)
    return


@app.cell
def _(L, o):
    compose = L("f", "g", "h", "x").o("f", o("g", o("h", "x"))).build()
    forward = L("f", "g", "h", "x").o("f", "g", "h", "x").build()
    return compose, forward


@app.cell
def _(compose):
    compose
    return


@app.cell
def _(forward):
    forward
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cool right ?

    ## mysterious function

    Let's go back to our mysterious function:
    """)
    return


@app.cell
def _(s_myst):
    s_myst
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It turns out that this function implements the multiplication of church numbers.

    Let's try it out:
    """)
    return


@app.cell
def _(four, s_myst, three):
    s_myst(three)(four)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wait, what is this monstruosity ?

    Well, it's a term. It does not have a $\lambda$ at the top, so it's clearly not a lambda function. It's still a term, a term that bundles together `s_myst`, `two` and `three`.

    But this not what we want. We want to know what is the *result* of this operation.

    Right now, we can't. We did not specify how this is supposed to be transformed. We need a way to run it, like in python: a **semantic**.

    Don't worry, I have implemented it. Let's jump directly to the result:
    """)
    return


@app.cell
def _(s_myst, three, two):
    s_myst(two)(three).reduce()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And indeed, we get 6.

    But you may wonder (and you should): how did we go from the monstruosity to the nice "6" result ?

    I spent weeks animating this stuff, so I hope you will enjoy it (for lack of understanding it, at least for now).

    Click on the left and right arrow to navigate, click on the figure to animate.
    """)
    return


@app.cell
def _(four, mo, s_myst, three):
    mo.carousel([x.show_beta() or x for x in s_myst(three)(four).reduction_chain()])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # The beta reduction
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As one dives deeper into the formalism and the internals of lambda-calculus, it's easy to get lost.
    To make it easier, it's fundamental to hold back to what we know already. And what do we know already: how python functions work ! Or at least, we can have a pretty good idea.

    So let's take an example, and let's think about "how would python calculate it"

    Here is the term we will analyse:

    $$
    \lambda n \lambda f \lambda x. f (n f x)
    $$

    If you want, click below to know what this function compute. If you prefer trying to guess it as we detail each step of the calculation, don't.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    _spoiler = mo.md(r"""
    This function is the *successor* function. It takes a church numeral (e.g two = $\blue{\lambda f \lambda x. f(f(x))}$) and returns the next church numeral (e.g three = $\blue{\lambda f \lambda x. f(f(f(x)))}$)
    """)
    mo.md(rf"""
    <details>
        <summary>Spoiler: what does this function compute ?</summary>
    {_spoiler.text}
    </details>
    """)
    return


@app.cell
def _(L, o, one):
    succ = L("n", "f", "x").o("f", o("n", "f", "x")).build()
    stuff_to_compute = succ(one)
    stuff_to_compute
    return stuff_to_compute, succ


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and here is the python version:
    """)
    return


@app.cell
def _():
    succ_py = lambda n: lambda f: lambda x: f(n(f)(x))
    one_py = lambda f: lambda x: f(x)
    # TODO: compute `succ_py(one_py)`
    return


@app.cell(hide_code=True)
def _(mo):
    _solution = mo.md(r"""
    To compute `succ_py(one_py)`, the key is to **replace** the variable `n` in `succ_py`

    Since we pass `one_py` as the argument, we must replace `n` by `one_py`.

    Let's do it:

    ```
    # before
    lambda n: lambda f: lambda x: f(n(f)(x))

    # after
    lambda f: lambda x: f((  lambda f: lambda x: f(x)    )(f)(x))
    ```

    It starts to be hard to see, so let's use the more math-y representation:

    $$
    \big (\green{\lambda n} \lambda f \lambda x. f(\green{n} f x) \big)(\blue{\lambda f \lambda x .f(x)})\\
    \downarrow  \\
    \lambda f \lambda x f((\blue{\lambda f \lambda x. f(x)}) f x) \\
    $$

    When you see the pattern, it starts to make sense.

    The first agument was $\green n$, and since we have *provided* this argument with the value, $\blue{\lambda f \lambda x .f(x)}$, we replace each *occurence* of $\green n$ with $\blue{\lambda f \lambda x .f(x)}$
    """)

    mo.md(rf"""
    ## Challenge 4

    Try to find what the first step is for python to compute `succ_py(one_py)`

    <details>
    <summary>Solution</summary>
    {_solution.text}
    </details>

    Once you feel like you understand, I invite you to look at the animated version below. It's exactly the same thing, just with blocks instead of letters.
    """)
    return


@app.cell
def _(stuff_to_compute):
    stuff_to_compute.show_beta()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, we have a new expression. Let's rewrite it here:

    $$
    \lambda f \lambda x. f\big((\lambda f \lambda x. f(x)) f x\big)
    $$

    If you prefer the python version:
    ```py
    lambda f: lambda x: f(lambda f: lambda x: f(x))(f)(x)
    ```

    There is something spooky going on here: `lambda f` twice and `lambda x` twice. We can apply a trick: *renaming*

    ```py
    lambda f: lambda x: f(lambda f1: lambda x1: f1(x1))(f)(x)
    ```

    It's easy to get lost and to rename the wrong thing. Hopefully, our graphical representation do not have this problem. Instead of having to "rename", we have to "reconnect" the variables to the right block.

    ## Aside: renaming

    Let's consider this expression:

    $$
    \big(\lambda f. f(f(f))\big)(\blue{\lambda x \lambda y .x})
    $$

    When we apply the first operation, we get this (quite long) expression:


    $$
    (\blue{\lambda x \lambda y .x})\big((\blue{\lambda x \lambda y .x})(\blue{\lambda x \lambda y .x})\big)
    $$

    But $x$ and $y$ don't have the same role in the first group, in the second group and in the third group. So we could rename it, just like the previous example:

    $$
    (\blue{\lambda x1 \lambda y1 .x1})\big((\blue{\lambda x2 \lambda y2 .x2})(\blue{\lambda x3 \lambda y3 .x3})\big)
    $$

    Now compare this with the graphical representation:
    """)
    return


@app.cell
def _(L):
    _a = L("f").o("f", "f", "f").build()
    _b = L("x", "y").o("x").build()
    _a(_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We don't have to rename anything, because the blue blocks (corresponding to $\lambda x \lambda y$) are duplicated, and the new red blocks (the variables) are connected to the right blue blocks.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## Challenge 5

    Let's go back to our expression. After the first step, we arrived at:

    ```py
    lambda f: lambda x: (lambda f1: lambda x1: f1(x1))(f)(x)

    # it's a bit hard to read, so let's rewrite it:
    def lambda_(f):
        def lambda_(x):
            inside_block = lambda f1: lambda x1: f1(x1)
            return f(inside_block(f)(x))
        return lambda_
    ```

    Do you see a way to simplify this function, meaning to write a simpler function that does exactly the same thing ?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <details>
    <summary>
    Solution:
    </summary>
    ```py
    lambda f: lambda x: f(f(x))
    ```

    The exterior block takes "f" and "x", and forward them to the interior block.
    The interior block takes "f", renames it as "f1", takes "x", renames it as "x1", and return "f(x)"
    Last step: the exterior block takes the result from the interior block "f(x)" and calls f a last time: "f(f(x))"
    </details>

    You can now look at the corresponding animations:
    """)
    return


@app.cell
def _(mo, stuff_to_compute):
    mo.carousel([x.show_beta() or x for x in stuff_to_compute.beta().reduction_chain()])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Congratulations ! You just understood how lambda calculus works.

    Let's give a name to the operation used to go from one term to the next: **beta-reduction**.

    We note it like this:

    $$
    \big (\green{\lambda n} \lambda f \lambda x. f(\green{n} f x) \big)(\blue{\lambda f \lambda x .f(x)})
    \rightarrow_{\beta}
    \lambda f \lambda x f((\blue{\lambda f \lambda x. f(x)}) f x)
    $$

    To discuss beta-reduction even more precisely, we need to introduce a little more terminology.

    Let's take this expression:

    $$\big (\green{\lambda n} \lambda f \lambda x. f(\green{n} f x) \big)(\blue{\lambda f \lambda x .f(x)})$$

    The entire formula is called a redex (the stuff we want to reduce). The $\green{\lambda n}$ is the root-lambda of the redex, and $\blue{\lambda f \lambda x. f(x)}$ is the argument of the redex.

    Each $\green n$ appearing in the term is an occurence "bound to the root-lambda".

    To recap, the algorithm is:
    - find a redex of the form $(\green \lambda \green x E)(\blue{A})$
    - replace every occurence of $E$ that is bound to the root lambda with a copy of $\blue A$
    - each time you replace, rename all the variables that you need to rename (\*)
    - remove $\green{\lambda x}$ and $\blue A$


    > Note: I did not detail all the cases for the renaming step. It's subtle: you have to rename a variable only if it's bound to the root lambda of the argument $\blue A$, because you don't want to change variables that appear higher in the tree.

    There is an important thing to note here: I said find **a** redex and not take **the** redex. We have already seen this in action, but you may not have paid attention. Look back at:
    """)
    return


@app.cell
def _(stuff_to_compute):
    stuff_to_compute.beta().beta()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the graphical representation, the redexes appear in blue with a yellow border. (this makes sense: it's a lambda (blue) with an argument (yellow)).

    Here, the redex is not at the top of the expression, it's somewhere inside.

    But it can be even worse, for example:
    """)
    return


@app.cell
def _(L):
    _e = L("y").o(L("x").o("x"), "y")
    L("f").o("f", _e, _e).build()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here, we have 2 potentials redex to chose from to do our lambda-reduction. Which one do we chose ?

    It does not matter. Well, it does matter, but ... it does not *really* matter.

    Let me introduce: termination and the Church-Rosser Theorem
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Termination and the Church-Rosser theorem

    All the terms I used from the beginig were really nice: they simplified (more precisely, beta-reduced) until they reached a very simple form: a form with no potential redex.

    Is it always the case ? It might surprise you, but no. There is even a simple expression that **never stop reducing**.

    Here it is:

    $$
    \bigg (\lambda f. f(f)\bigg)\bigg(\lambda g. g(g))\bigg)
    $$

    ## Challenge 6: Try to reduce this expression, and see what happens.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    solution = mo.md(r"""
    $$
    \bigg (\green{\lambda f}. \green f(\green f)\bigg)\bigg(\blue{\lambda g. g(g)})\bigg) \rightarrow_{\beta}
    (\lambda g. g(g))(\lambda g. g(g))) \rightarrow
    (\lambda f. f(f))(\lambda g. g(g)))
    $$

    This expression reduces to itself !
    """)

    mo.md(rf"""
    <details>
        <summary>
        Solution
        </summary>
        {solution.text}
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now for the animated version:
    """)
    return


@app.cell
def _(L):
    omega = L("f").o("f", "f").build()
    omega(omega).show_beta()
    return (omega,)


@app.cell(hide_code=True)
def _(mo):
    bomb_button = mo.ui.run_button(
        label="Run the python version of the expression", kind="danger"
    )
    return (bomb_button,)


@app.cell(hide_code=True)
def _(bomb_button, mo):
    mo.md(rf"""
    And it's not just something funny in our rules: the exact same thing appens in python (click on the button to run):

    {bomb_button}
    """)
    return


@app.cell
def _(bomb_button):
    if bomb_button.value:
        (lambda f: f(f))(lambda g: g(g))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Time for a recap:
    - A lambda-term can have zero, one or multiple "redexes" of the form $(\green{\lambda x}. E)(\blue A)$
      - if it has zero redex, we can't reduce it: we're done. Let's call it the "final form"
    - We can "beta-reduce" a term
      - start by chosing a redex if they are multiple
      - apply the procedure to transform the redex. You get a new term
    - Some terms are "nice". A "nice" term:
      - has a single redex
      - reduces to a term that has a single redex, and we can keep reducing ...
      - reaches a "final form" if we reduce enough times
    - This means that:
      - some terms are not nice because they have multiple redexes
      - some terms are not nice because they never reduce to a final form.

    How do we handle "not nice" tems ?

    How do we chose the right redex to reduce ?

    Will this change the result ?

    How do we know if a term will eventually reach a final form ?

    This is the kind of questions that the creators of lambda-calculus have asked themselves. And since they were mathematicians, they have worked very hard to get answers.

    Let's discuss three fundamental theorems of lambda-calculus
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Church-Rosser theorem

    The [Church-Russer Theorem](https://en.wikipedia.org/wiki/Church%E2%80%93Rosser_theorem) states that if you take a term, and start applying beta-reductions in two different ways, you can't find completely different results.

    More precisely, if Alice applies some number of reductions until she reaches A, and if Bob applies some other number of reductions until he reaches B, there is a way to keep applying reductions to A and B until they become exactly the same.

    It **DOES NOT MEAN** that you can pick the beta-reductions at random. It's possible that Alice is smart and find a way to reduce to a final form, and Bob is dumb and keep reducing forever, because he chose the wrong regex each time. But at each step, if Bob becomes smart, he can reach a final form.

    It **DOES** mean that there is only one possiblef final form. We call it **the** [normal form](https://en.wikipedia.org/wiki/Normal_form_(abstract_rewriting))

    Below is an example where the choice of redex matters.

    ## Challenge 7

    find a strategy to reduce to a normal form, and a strategy to keep reducing forever.

    $$
    (\lambda a \lambda b. b) \bigg((\lambda f. f(f))(\lambda g. g(g))\bigg) \big(\lambda f\lambda x. f(x)\big)
    $$


    If you prefer the graphical version:
    """)
    return


@app.cell
def _(l_true, omega, one):
    l_true(omega(omega))(one)
    return


@app.cell(hide_code=True)
def _(mo):
    _solution = mo.md(r"""
    If you start by reducing the **outer** redex two times, you will drop the big expression in the middle.


    $$
    (\green {\lambda a} \lambda b. b) \bigg(\blue{(\lambda f. f(f))(\lambda g. g(g))}\bigg) \big(\lambda f\lambda x. f(x)\big) \\
    \downarrow_\beta \\
    (\lambda b. b) \sout {\bigg((\lambda f. f(f))(\lambda g. g(g))\bigg)} \big(\lambda f\lambda x. f(x)\big) \\
    \downarrow_\beta \\
    \lambda f\lambda x. f(x)
    $$

    But if you reduce the inner redex, you get the same term. You can go on forever:

    $$
    (\lambda a \lambda b. b) \bigg((\green{\lambda f}. \green f(\green f))(\blue{\lambda g. g(g)})\bigg) \big(\lambda f\lambda x. f(x)\big) \\
    \downarrow_\beta \\
    (\lambda a\lambda b. b) \bigg((\lambda f. f(f))(\lambda g. g(g))\bigg) \big(\lambda f\lambda x. f(x)\big) \\
    $$

    """)
    mo.md(rf"""
    <details>
        <summary>
            Solution
        </summary>
        {_solution.text}
    </details>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The leftmost-outermost reduction is normalizing

    This looks crazy, but it is simpler than the first theorem.

    This theorem states that the smart way to reduce is to take the first redex.

    *leftmost-outermost* is a fancy way to say "the first lambda you see"

    If you use this reduction each time, you know that you will get the final form **IF IT EXISTS**.

    This is the reduction I implemented in the graphical animations on this page.

    For example, we can see that the redution of the previous expression (challenge 7) reaches the final form:
    """)
    return


@app.cell
def _(l_true, mo, omega, one):
    mo.carousel(
        [x.show_beta() or x for x in l_true(omega(omega))(one).reduction_chain()]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Turing-completeness and the halting problem

    Now for the really cool stuff.

    How do we know if a term will reach its normal form (in this case, we say the reduction "terminates") ?

    Well, we can't !

    The only way is to keep applying the ~~outermost-leftmost~~ smart reduction and hope we reach the final form one day.

    The reason why it's impossible to know is that lambda-calculus is Turing-complete. We can do absolutely any computation with the right term at the start.

    You can take a program written in C, and transform it into a lambda-term that will do exactly the same thing.
    This is not a joke ! Someone even created [compiler from c to lambda-calculus](https://github.com/woodrush/lambda-8cc) 🤯

    And since we can't know if a program will stop or not, we can't know if a lambda-term will reach a normal form.

    If you don't know already why it is the case, go watch this video on the **Halting problem**:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.iframe("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/macM_MtS_w4?si=8Si42HgYCGqUMhpx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Bonus content

    This part if for the lambda-calculus hypsters.
    """)
    return


@app.cell
def _(L, o):
    pred = (
        L("n", "f", "x")
        .o(
            "n",
            L("g", "h").o("h", o("g", "f")),
            L("u").o("x"),
            L("u").o("u"),
        )
        .build()
    )
    pred
    return (pred,)


@app.cell
def _(pred, two):
    pred(two).reduce()
    return


@app.cell
def _(L, l_false, l_true):
    pair = L("a", "b", "x").o("x", "a", "b").build()
    first = L("x").o("x", l_false).build()
    second = L("x").o("x", l_true).build()
    pair
    return first, pair, second


@app.cell
def _(L, four, o, three):
    sum = L("n", "m", "f", "x").o(o("n", "f"), o("m", "f", "x")).build()
    sum(four)(three).reduce()
    return (sum,)


@app.cell
def _(L, first, o, pair, second, sum):
    fib_pair = (
        L("p").o(pair, o(sum, o(first, "p"), o(second, "p")), o(first, "p")).build()
    ).reduce()
    fib_pair
    return (fib_pair,)


@app.cell
def _(fib_pair, four, one, pair, succ, zero):
    five = succ(four)
    five(fib_pair)(pair(one)(zero)).reduce()
    return


@app.cell
def _(L, o):
    fact = (
        L("n", "f").o(
            "n",
            L("f", "n").o("n", o("f", L("f", "x").o("n", "f", o("f", "x")))),
            L("x").o("f"),
            L("x").o("x"),
        )
    ).build()
    fact
    return (fact,)


@app.cell
def _(L, o):
    # the Y combinator
    y = (
        L("f").o(
            L("g").o("f", o("g", "g")),
            L("g").o("f", o("g", "g")),
        )
    ).build()
    y
    return (y,)


@app.cell
def _(fact, four):
    fact(four).reduce()
    return


@app.cell
def _(fact, mo, three):
    mo.carousel([x for x in fact(three).reduction_chain()])
    return


@app.cell
def _(L, first, l_false, l_true, o, pair, second, succ, zero):
    div2 = (
        L("n")
        .o(
            "n",
            L("p").o(
                o(second, "p"),
                o(pair, o(first, "p"), l_true),
                o(pair, o(succ, o(first, "p")), l_false),
            ),
            o(pair, zero, l_false),
        )
        .build()
        .reduce()
    )
    div2
    return (div2,)


@app.cell
def _(div2, mo, three):
    # divide three by 2 in 51 steps
    mo.carousel([x for x in div2(three).reduction_chain()])
    return


@app.cell
def _(L, first, o, pair, second):
    pack = L("f", "p").o("f", o(first, "p"), o(second, "p")).build().reduce()
    unpack = L("f", "a", "b").o("f", o(pair, "a", "b")).build()
    pack
    return


@app.cell
def _(div2, four, succ):
    len(list((div2(succ(succ((four))).reduce()).reduction_chain())))
    return


@app.cell
def _(div2, four):
    div2(four).reduce()
    return


@app.cell
def _(L, l_false, l_true, o):
    mult = L("n", "m", "f", "x").o("n", o("m", "f"), "x").build()
    is_not_zero = L("n").o("n", L("f").o(l_true), l_false).build().reduce()
    return is_not_zero, mult


@app.cell
def _(
    L,
    div2,
    first,
    is_not_zero,
    mult,
    o,
    pair,
    second,
    succ,
    three,
    y,
    zero,
):
    syracuse = y(
        L("F", "n")
        .o(
            o(
                L("half_and_reminder").o(
                    o(is_not_zero, o(first, "half_and_reminder")),
                    zero,  # ?
                    o(
                        pair,
                        "n",
                        o(
                            "F",
                            o(
                                o(second, "half_and_reminder"),
                                # even: n / 2
                                o(first, "half_and_reminder"),
                                # odd: 3 * n + 1
                                o(succ, o(mult, three, "n")),
                            ),
                        ),
                    ),
                ),
                o(div2, "n"),
            )
        )
        .build()
    )
    syracuse
    return


@app.cell
def _():
    # run at your own risks ...
    # syracuse(five).reduce()
    return


if __name__ == "__main__":
    app.run()
