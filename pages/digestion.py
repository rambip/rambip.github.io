import marimo

__generated_with = "0.19.4"
app = marimo.App(width="medium", css_file="../assets/language.css")

with app.setup(hide_code=True):
    import marimo as mo
    FR_SOURCE = mo.watch.file("markup/digestion_fr.md")
    EN_SOURCE = mo.watch.file("markup/digestion_en.md")
    def page_():
        from here import Embed

        return Embed(__file__, globals()["app"], "Digestive problems", include=[FR_SOURCE, EN_SOURCE])


@app.cell(hide_code=True)
def _():
    lang_selector = mo.Html(
        """
        <input type="radio" name="language" id="english" class="lang-toggle" checked>
        <input type="radio" name="language" id="french" class="lang-toggle">

        <nav class="tabs">
          <label for="english" class="tab-label">English</label>
          <label for="french" class="tab-label">Français</label>
        </nav>
        """
    )

    def multilang(english_content, french_content):
        en_html = mo.as_html(english_content).text
        fr_html = mo.as_html(french_content).text
        return mo.Html(f"""
        <article id="doc-en" class="document">
        {en_html}
        </article>

        <article id="doc-fr" class="document">
        {fr_html}
        </article>
        """)
    return lang_selector, multilang


@app.cell
def _(lang_selector):
    lang_selector
    return


@app.cell(hide_code=True)
def _(multilang):
    multilang(mo.md(EN_SOURCE.read_text()), mo.md(FR_SOURCE.read_text()))
    return


@app.cell(hide_code=True)
def _(multilang):
    multilang(
        mo.md("""
    # Appendices

    ## Food list

    Below is a list of a wide variety of food, whith each of them how much I tolerate it.

    Caption:
    - ❌ = avoid
    - 🫤 = limit (but typically fine)
    - 😋 = enjoy
    - ❓ = not tested in long time, must retry
    """),
        mo.md("""
    # Annexes

    ## Liste alimentaire

    Ci dessous une liste d'aliments que je supporte plus ou moins.

    Légende:
    - ❌ = éviter
    - 🫤 = limiter
    - 😋 = sans modération
    - ❓ = pas tésté depuis longtemps, à réessayer
    """)
    )
    return


@app.cell(hide_code=True)
def _():
    import requests
    import polars as pl

    scores = {
        "❌": 0,
        "🫤": 1,
        "😋": 2,
        "❓": 3,
    }
    df = pl.DataFrame(
        requests.get(
            "https://docs.getgrist.com/api/docs/pGUZjNpq5EZBKfZHCRjZBi/tables/Aliments/records"
        ).json()["records"]
    ).select(pl.col("fields").struct.unnest()).sort(pl.col("Amount").replace(scores))

    with pl.Config() as cfg:
        cfg.set_tbl_rows(-1)
        cfg.set_tbl_hide_dataframe_shape(True)
        cfg.set_tbl_hide_column_data_types(True)
        table = mo.Html(df._repr_html_())
    

    table
    return


if __name__ == "__main__":
    app.run()
