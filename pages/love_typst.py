import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")

with app.setup:
    # Initialization code that runs before all other cells
    import marimo as mo
    import typst as typst_lib


@app.function(hide_code=True)
def page_():
    from here import Embed

    return Embed(__file__, globals()["app"], "The greatest markup language")


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    I 💖 [typst](https://typst.app/)
    """)
    return


@app.cell
def _():
    header = """
    #set page(width: auto, height: auto, margin: 10pt)
    #set text(size: 20pt)
    """

    def typst_math(input):
        source = (header + input).encode("utf-8")
        svg = typst_lib.compile(source, format="svg")
        return mo.Html(svg.decode("utf-8"))

    return (typst_math,)


@app.cell
def _(typst_math):
    typst_math("$(oo -> oo) / (1 eq 1)$")
    return


@app.function
def sandwiches():
    source = """
    #import "@preview/cetz:0.4.2": canvas, draw

    #set page(height: auto, margin: 1cm)

    #let colors = (blue, red, green, purple, orange, yellow, teal, maroon)

    #let up = (0, 0, 1)
    #let down = (0, 0, -1)
    #let east = (1, 0, 0)
    #let west = (-1, 0, 0)
    #let north = (0, 1, 0)
    #let south = (0, -1, 0)

    #let vec-scale = 0.8
    #let rot-z = 20deg
    #let tilt = 80deg

    #let transform(x, y, z) = {
      let x1 = x * calc.cos(rot-z) - y * calc.sin(rot-z)
      let y1 = x * calc.sin(rot-z) + y * calc.cos(rot-z)
      let z1 = z
      let y2 = y1 * calc.cos(tilt) - z1 * calc.sin(tilt)
      let z2 = y1 * calc.sin(tilt) + z1 * calc.cos(tilt)
      (x1, -y2)
    }

    #let draw-vector(anchor, vec, color) = {
      let o = transform(..anchor)
      let end-pt = (anchor.at(0) + vec.at(0), anchor.at(1) + vec.at(1), anchor.at(2) + vec.at(2))
      let e = transform(..end-pt)
      draw.set-style(mark: (end: (symbol: ">")))
      draw.line(o, e, stroke: (paint: color, thickness: 2pt))
    }

    #let draw-tangents(vecs) = {
      for (i, t) in vecs.enumerate() {
        let scaled-vec = (t.vector.at(0) * vec-scale, t.vector.at(1) * vec-scale, t.vector.at(2) * vec-scale)
        draw-vector(t.anchor, scaled-vec, colors.at(i))
        draw.circle(transform(..t.anchor), radius: 0.08, fill: black)
      }
    }

    #let draw-on-sphere(vecs) = {
      let r = 2
      let n = 30

      // Latitude lines
      for i in range(0, 9) {
        let lat = (i - 4) * 20deg
        let r-lat = r * calc.cos(lat)
        let z = r * calc.sin(lat)
        let pts = ()
        for j in range(0, n + 1) {
          let lng = j * 360deg / n
          pts.push(transform(r-lat * calc.cos(lng), r-lat * calc.sin(lng), z))
        }
        draw.line(..pts, stroke: (paint: gray.darken(20%), thickness: 0.5pt))
      }

      // Longitude lines
      for i in range(0, 8) {
        let lng = i * 360deg / 8
        let pts = ()
        for j in range(0, n + 1) {
          let lat = (j - n/2) * 180deg / n
          pts.push(transform(
            r * calc.cos(lat) * calc.cos(lng),
            r * calc.cos(lat) * calc.sin(lng),
            r * calc.sin(lat)
          ))
        }
        draw.line(..pts, stroke: (paint: gray.darken(20%), thickness: 0.5pt))
      }

      // Draw tangent points on sphere
      for (i, t) in vecs.enumerate() {
        let vec = t.vector
        let norm = calc.sqrt(vec.at(0)*vec.at(0) + vec.at(1)*vec.at(1) + vec.at(2)*vec.at(2))
        let pole = transform(r * vec.at(0)/norm, r * vec.at(1)/norm, r * vec.at(2)/norm)
        draw.circle(pole, radius: 0.15, fill: colors.at(i), stroke: colors.at(i))
      }
    }

    #let draw-plane(offset: (0, 0, 0), fill-color: rgb("#e8e8e8")) = {
      let base-corners = ((-1.5, -1, 0), (1.5, -1, 0), (1.5, 1, 0), (-1.5, 1, 0))
      let corners = base-corners.map(c => transform(
        c.at(0) + offset.at(0),
        c.at(1) + offset.at(1),
        c.at(2) + offset.at(2)
      ))
      draw.line(..corners, close: true, fill: fill-color, stroke: black)
    }

    #let draw-cube() = {
      let cube-pts = (
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
      )
      let edges = ((0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7))
      for (i, j) in edges {
        draw.line(transform(..cube-pts.at(i)), transform(..cube-pts.at(j)), stroke: black)
      }
    }

    #let draw-cylinder(axis: 2, height: 2, radius: 1) = {
      let n = 30

      // Generate circle points based on axis
      let circle-pts(z-val) = {
        let pts = ()
        for i in range(0, n + 1) {
          let angle = i * 360deg / n
          let x = radius * calc.cos(angle)
          let y = radius * calc.sin(angle)

          if axis == 0 {
            pts.push((z-val, x, y))
          } else if axis == 1 {
            pts.push((x, z-val, y))
          } else {
            pts.push((x, y, z-val))
          }
        }
        pts
      }

      let bottom-z = -height / 2
      let top-z = height / 2

      // Draw top and bottom circles
      draw.line(..circle-pts(bottom-z).map(p => transform(..p)), close: true, stroke: black)
      draw.line(..circle-pts(top-z).map(p => transform(..p)), close: true, stroke: black)

      // Draw connecting lines (every few steps for clarity)
      for i in range(0, n, step: 4) {
        let angle = i * 360deg / n
        let x = radius * calc.cos(angle)
        let y = radius * calc.sin(angle)

        let bottom = none
        let top = none

        if axis == 0 {
          bottom = (bottom-z, x, y)
          top = (top-z, x, y)
        } else if axis == 1 {
          bottom = (x, bottom-z, y)
          top = (x, top-z, y)
        } else {
          bottom = (x, y, bottom-z)
          top = (x, y, top-z)
        }

        draw.line(transform(..bottom), transform(..top), stroke: black)
      }
    }

    #let mid = [#set text(size: 40pt); #sym.arrow.double]

    // Row 1: Single upward vector
    #{
      let vecs = ((anchor: (0, 0, 0), vector: up),)
      grid(columns: (1fr, 20pt, 1fr), align: center+horizon,
        canvas(length: 1.3cm, {
          draw-plane()
          draw-tangents(vecs)
        }),
        mid,
        canvas(length: 1.3cm, { draw-on-sphere(vecs) })
      )
    }

    #pagebreak()

    // Row 2: Opposing vectors (parallel planes)
    #{
      let vecs = (
        (anchor: (0, 0, -1), vector: up),
        (anchor: (0, 0, 1), vector: down)
      )
      grid(columns: (1fr, 20pt, 1fr), align: center+horizon,
        canvas(length: 1.3cm, {
          draw-plane(offset: (0, 0, -1))
          draw-plane(offset: (0, 0, 1), fill-color: rgb("#d8d8d8"))
          draw-tangents(vecs)
        }),
        mid,
        canvas(length: 1.3cm, { draw-on-sphere(vecs) })
      )
    }

    #pagebreak()

    // Row 3: Cylinder
    #{
      let vecs = (
        (anchor: (0, 0, 1), vector: up),
      )
      grid(columns: (1fr, 20pt, 1fr), align: center+horizon,
        canvas(length: 1.3cm, {
          draw-cylinder(axis: 2, height: 2, radius: 1)
          draw-tangents(vecs)
        }),
        mid,
        canvas(length: 1.3cm, { draw-on-sphere(vecs) })
      )
    }

    #pagebreak()

    // Row 4: Cube with inverted vectors
    #{
      let vecs = (
        (anchor: up, vector: down),
        (anchor: down, vector: up),
        (anchor: east, vector: west),
        (anchor: west, vector: east)
      )
      grid(columns: (1fr, 20pt, 1fr), align: center+horizon,
        canvas(length: 1.3cm, {
          draw-cube()
          draw-tangents(vecs)
        }),
        mid,
        canvas(length: 1.3cm, { draw-on-sphere(vecs) })
      )
    }
"""
    out = typst_lib.compile(source.encode("utf-8"), format="svg")
    return [mo.Html(p.decode("utf-8")) for p in out]


@app.cell
def _():
    sandwiches()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
