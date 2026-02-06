# AGENTS.md

## Project Goal

Personal website built entirely from **marimo notebooks** to share interactive computational notebooks, art, creative coding, blog posts, and academic work. Everything is executable Python code compiled into a static website.

## Main Idea & Marimo

**Marimo** is a reactive Python notebook framework where notebooks are pure Python files (`.py`), cells auto-execute when dependencies change, and outputs stay synchronized with code. This project uses marimo to write content as interactive notebooks, execute them programmatically, and export to static HTML while maintaining everything as version-controlled code.

## Codebase Structure

- **`pages/`** - Marimo notebooks that become pages. `home.py` is the build entry point
- **`src/here/`** - Build system core (the pun: `from here import ...`)
- **`markup/`** - Jinja2 templates, markdown files, Typst documents
- **`assets/`** - CSS, JavaScript, fonts, images
- **`web/`** - Generated output (git-ignored)

## The "here" Module

The deliberate pun lets notebooks do `from here import stuff`. It provides:

**Classes:**
- `Embed(path, app, title, children, url, include)` - Wraps notebook for execution
  - Executes and caches notebook state (using `cachier` → `.cache/`)
  - Can execute self, all children, or just children
- `NotebookState` - Cached execution result before rendering
  - Contains: title, url, code, outputs, python content
  - Can render to HTML with template

**Utilities:**
- `me()` - Personal info
- `asset(path)` - Load media assets
- Path constants: `PATH_WEB`, `PATH_PAGES`, `PATH_ASSETS`, `PATH_MARKUP`

**Design:** Small API surface, separation of execution (cached) vs rendering (not cached), composable notebook trees.

## Build Process

**Run:** `mise run build` (see `mise.toml` for task definitions)

**Flow:**
1. `mise run build` executes `pages/home.py` using `uv run`
2. `home.py` imports all page modules and creates an `Embed` tree with children
3. For each child notebook:
   - Execute notebook with marimo's AppScriptRunner
   - Capture code outputs and stdout
   - Cache result by content hash (`.cache/` directory)
   - Return `NotebookState` object
4. For each `NotebookState`:
   - Load Jinja2 template from `markup/`
   - Pass notebook data + context flags to template
   - Render final HTML
   - Write to `web/` directory
5. Home page rendered last with special context (different navbar)

**Cache:** Changing templates only re-renders. Changing notebook code re-executes. Clear cache: `rm -rf .cache`

## uv

Project uses **uv** for Python dependency management and execution:
- Fast, reliable Python package installer
- All code runs via `uv run` (see `mise.toml`)
- Dependencies synced with `mise run sync`

## Marimo Notebook Template

Basic structure for a page notebook:

```python
import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")

with app.setup(hide_code=True):
    def page_():
        from here import Embed
        return Embed(__file__, globals()["app"], "Page Title")

@app.cell
def _():
    import marimo as mo
    return (mo,)

@app.cell
def _(mo):
    mo.md("# Your content here")
    return

if __name__ == "__main__":
    app.run()
```

Key points:
- `page_()` function in setup cell returns `Embed` instance
- Access `app` via `globals()["app"]`
- Use `mo` for marimo utilities (markdown, HTML, etc.)

## Other Technologies

**Typst:** Modern markup for PDFs (LaTeX alternative), embedded in notebooks

**Python Libraries (for notebook content):**
- **polars** - Fast DataFrames (preferred over pandas)
- **altair** - Declarative visualizations

`TODO.md` exists but is rarely current. Ask the human for priorities.

## Coding Style

- **Concision** - Short, clear code over verbose explanations
- **Assertions** - Use `assert` instead of try/except for invariants
- **Refactor continuously** - Question: "Can this be simpler?"
- **Small API** - Remove abstractions that don't pull weight
- **Comments explain "why"** - Code shows "what"

## Interaction Rules

When working on this project:

1. **Ask questions** when unclear (better than assumptions)
2. **Simplify, not just add** - Look for opportunities to reduce complexity
3. **Ask before running** - "Should I run `mise run build`?" or "Clear cache?"
4. **Prioritize maintainability** - Small, clear changes over clever solutions
5. **Stay concise** - In code and communication
