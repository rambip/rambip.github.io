import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    return go, make_subplots, mo, np


@app.function(hide_code=True)
def page_():
    from here import include
    return include(__file__, globals()["app"], "Rubik's cube emulation in 10 lines of numpy")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The core logic
    This create a permutation inside a tensor of shape $5 \times N \times N \times N \times 3 \times 2$

    The idea is that the five parameters `(ix, iy, iz, d, a)` contains exactly the information about the location of a tiny cube:  at cell `(ix, iy, iz)`, oriented in direction `d`, and `a` indicates the way it points (up or down, right or left ...).

    Then, we can define a huge array, with one element for each position.

    Here comes the magic sauce: A configuration of the rubik's cube is just a particular permutation of this huge array !
    """)
    return


@app.cell
def _(np):
    arr = lambda shape, *x: np.array(x, dtype=int).reshape(shape)
    cho = lambda *s: np.random.choice(*s, replace=False)
    i3 = arr((3,), 0, 1, 2)

    solved = lambda n: np.indices((n, n, n, 3, 2))


    def move(n, i, d, d1, d2):
        # create the random permutation
        s = solved(n)
        result = s
        idx = [slice(n)] * 3
        idx[d] = i
        result[d1, *idx] = s[d2, *idx]
        result[d2, *idx] = n - 1 - s[d1, *idx]
        result[-2, *idx, [d1, d2]] = s[-2, *idx, [d2, d1]]
        result[-1, *idx, d1] = 1 - s[-1, *idx, d2]
        return result
    return arr, cho, i3, move, solved


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Then, we need a code to display our cube.
    """)
    return


@app.cell
def _(arr):
    COLORS = arr((3, 2, 3), *"002010220222200210") / 2
    SQUARE = arr((4, 3), *"000010110100")
    return COLORS, SQUARE


@app.cell
def _(COLORS, SQUARE, arr, go, i3, make_subplots, move, np, solved):
    def display_plotly(cube):
        N = cube.shape[1]
        traces = []

        for d in i3:
            for p in np.ndindex(N, N, N):
                if p[d] == 0:
                    s = SQUARE.copy()
                    s[:, [2, d]] = s[:, [d, 2]]
                    x, y, z = (s + p).T
                    losange = arr((2, 4), x - z, x - 2 * y + z)
                    c = COLORS[*cube[-2:, *p, d, 0]]*256
                    traces.append(go.Scatter(
                        x=list(losange[0]) + [losange[0,0]],
                        y=list(losange[1]) + [losange[1,0]],
                        fill="toself",
                        fillcolor=f"rgb({c[0]},{c[1]},{c[2]})",
                        line=dict(color="black", width=1),
                        mode="lines",
                        showlegend=False,
                    ))

        return traces

    r0 = solved(2)
    fig = make_subplots(rows=2, cols=3, specs=[[{'type': 'xy'}]*3]*2)

    for k, row_idx in zip([-1, 1], [1, 2]):
        for i in range(3):
            _m = move(2, 0, i, (i + k + 3) % 3, (i - k + 3) % 3)
            _traces = display_plotly(r0[:, *_m])

            for trace in _traces:
                fig.add_trace(trace, row=row_idx, col=i+1)

            fig.update_xaxes(range=[-4, 4], showticklabels=False, showgrid=False, zeroline=False, row=row_idx, col=i+1)
            fig.update_yaxes(range=[-6, 6], showticklabels=False, showgrid=False, zeroline=False, row=row_idx, col=i+1)

    fig.update_layout(width=900, height=600, plot_bgcolor='white', hovermode=False)
    fig
    return (display_plotly,)


@app.cell
def _(cho, display_plotly, go, i3, move, solved):
    r = solved(4)

    frames = []
    for t in range(40):
        traces = display_plotly(r)
        frames.append(go.Frame(data=traces, name=str(t)))
        m = move(4, cho(i3), *cho(i3, 3))
        r = r[:, *m]

    anim = go.Figure(data=frames[0].data, frames=frames)

    anim.update_xaxes(range=[-8, 8], showticklabels=False, showgrid=False, zeroline=False)
    anim.update_yaxes(range=[-12, 12], showticklabels=False, showgrid=False, zeroline=False)

    anim.update_layout(
        width=600,
        height=600,
        plot_bgcolor='white',
        hovermode=False,
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(
                label="Play", 
                method="animate", 
                args=[None, {"frame": {"duration": 300}, "transition": {"duration": 0}}]
            )]
        )]
    )

    anim
    return


if __name__ == "__main__":
    app.run()
