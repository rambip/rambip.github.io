import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")

with app.setup(hide_code=True):
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "Lambda Calculus primer")


@app.cell
def _():
    import polars as pl
    from curryparty import L, V
    import marimo as mo
    return L, V, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Lambda calculus

    You're tired of Turing Machines ?

    Your functionnal programming friends make fun of you because you don't know what a $\beta$-reduction is ?

    You think "currying" describes the action of adding spices to your dishes ?

    Then, you *absolutely* need to learn the basics of Lambda ($\lambda$)-Calculus

    ## What is this ?

    This is a personnal project I created from scratch, to fulfil the very specific mission of teaching lambda-calculus in an interactive, visual way.

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

    def print_one():
        print(1):
        return True

    print_one() # oh no, I dropped !
    print_one()

    ```

    > Solution :
    """)
    return


@app.cell
def _():
    # SOLUTION
    def o(x):
        print(0, end="")
        return x

    def i(x):
        print(1, end="")
        return x


    i(i(o(o(None))))
    return i, o


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This trick has additional benefits:
    """)
    return


@app.cell
def _(o):
    # second trick: pass functions instead of values
    def print_four_times(f):
        f(f(f(f(None))))

    print_four_times(o)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Challenge 1

    Write a function `boo` that print either `0` or `1`, depending on the argument. Remember, no condition and you can only pass functions !

    > Solution :
    """)
    return


@app.cell
def _(i, o):
    # SOLUTION

    def true(a, b):
        return a

    def false(a, b):
        return b

    def boo(side):
        return side(i, o)(None)

    boo(false)
    boo(true)
    return boo, false, true


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Why did I call these functions `true` and `false` instead of `left` and `right` ? Look at this mind-bending magic:
    """)
    return


@app.cell
def _(boo, false, true):
    def logical_not(x):
        return x(false, true)

    boo(logical_not(false))
    boo(logical_not(true))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Challenge 2

    Write a `logical_or` and a `logical_and` using the same structure as above.


    > Solution :
    """)
    return


@app.cell
def _(boo, false, true):
    # SOLUTION
    def logical_or(a, b):
        return a(a, b)

    def logical_and(a, b):
        return b(a, b)

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

    > Solution :
    """)
    return


@app.cell
def _(o):
    # SOLUTION

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
    """)
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
    What we call a "Lambda-function" or $\lambda$-function, is a mathematical description of the functions we were playing with in the last part.

    A lambda-function is "something with variables" that "return something".

    Let's create one:
    """)
    return


@app.cell
def _(L):
    L("x")._("x").build()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This is the simplest possible lambda function: a machine that takes `x` and returns `x`.

    In the graphical representation, the blue block means "taking x", the thin gray bar means "passing x" and the red block means "returning x".

    But a lambda can have multiple variables:
    """)
    return


@app.cell
def _(L):
    return_first = L("x", "y", "z")._("x").build()
    return_second = L("x", "y", "z")._("y").build()
    return_third = L("x", "y", "z")._("z").build()
    return_first, return_second, return_third
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Here, the first blue block means "take x", the second "take y" and the last "take z".

    The gray bar indicated which one will be returned. You can see that the name of the variables does not matter, and so they are not displayed on the illustration.

    It's a nice illustration of "curryfication": in lambda-calculus, no difference between a function that takes 2 arguments `a, b`, and a function that takes an argument `a`, and return a function that takes an argument `b`. Confused ? Look here:

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


    It's all well and good, but we're missing something. A lambda function can take arguments, return one of these arguments, but also **applying** (or *calling*) functions. Let's see that in action:
    """)
    return


@app.cell
def _(L):
    L("x", "f")._("f").call("x").build()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's unpack it.

    This lambda function takes a value `x` (first blue block), then a function `f` (second blue bock), use the function `f` (left gray line) and pass the `x` value (right gray line) to it (black horizontal line).

    For readability, the function that is called is under a black dot, and with a yello border.

    That's it ! With these 3 ingredients (blocks that take arguments, block that return arguments, block that apply), we can make any function we want. Before we go on, some terminology:
    - a "**Lambda**", or $\lambda$ , is a blue block. It corresponds to a single variable.
    - a "**Variable**" is a red block. It is "bound" to a specific lambda, indicated by a gray line
    - an "**Application**" is a horizontal black line. The function is the stuff inside the yellow border and the argument is at its right.
    - a "**Term**" is any combination of the above. If the thing at the top is a **Lambda**, it's called a lambda-function.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's define the $\lambda$-terms we already saw.
    """)
    return


@app.cell
def _(L):
    do_nothing = L("x")._("x").build()
    do_nothing # it's also called the "identity" function
    return


@app.cell
def _(L):
    l_false = L("a", "b")._("a").build()
    l_true = L("a", "b")._("b").build()
    l_false, l_true
    return


@app.cell
def _(L, V):
    zero = L("f", "x")._("x").build()
    one = L("f", "x")._("f").call("x").build()
    two = L("f", "x")._("f").call(V("f").call("x")).build()
    three = L("f", "x")._("f").call(V("f").call(V("f").call("x"))).build()
    zero, one, two, three
    return three, two


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Remember the "Church" functions ? In $\lambda$-calculus, they are called "Church numerals".

    With the above drawings, you can see how they work: they take `f`, then `x`, and then pass `x` through `f` a certain number of times. This number of times corresponds to the integer being represented.

    Let's try something harder:
    """)
    return


@app.cell
def _(L, V):
    s_myst = (
        L("number_a", "number_b", "f", "x")
        ._("number_a")
        .call(V("number_b").call("f"))
        .call("x")
        .build()
    )
    s_myst
    return (s_myst,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This starts to look a bit abstract, but with a bit of practice, these diagrams are easy to read. As an exercise, let's write the corresponding python function, just by looking at the diagram.

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


    ---

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
                    mo.md("# Composition"),
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
                    mo.md("# Forwarding"),
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
def _(L, V):
    compose = L("f", "g", "h", "x")._("f").call(V("g").call(V("h").call("x"))).build()
    forward = L("f", "g", "h", "x")._("f").call("g").call("h").call("x").build()
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
    This function implements the multiplication of church numbers.

    Let's try it out:
    """)
    return


@app.cell
def _(s_myst, three, two):
    s_myst(two)(three)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wait, what is this monstruosity ?

    Well, it's a term. It does not have $\lambda$ at the top, so it's clearly not a lambda function.

    But we did not specify how this is supposed to be transformed. We need a way to run it, like in python: a **semantic**.

    Don't worry, I have implemented it. It's as simple as:
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

    I spent weeks animating this stuff, so I hope you will enjoy it (for lack of understanding it, at least for now)
    """)
    return


@app.cell
def _(mo, s_myst, three, two):
    mo.carousel([x.show_beta() or x for x in s_myst(two)(three).reduction_chain()])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    TODO
    """)
    return


if __name__ == "__main__":
    app.run()
