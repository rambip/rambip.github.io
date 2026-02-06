# AGENTS.md

## Project Goal

This project is a personal website built entirely from **marimo notebooks**. It serves multiple purposes:
- Share interactive computational notebooks (data analysis, algorithms, visualizations)
- Publish art and creative coding projects
- Host blog posts and journal entries
- Showcase academic work and technical experiments

The unique aspect: everything is written as executable marimo notebooks that are then compiled into a static website.

## Main Idea & Marimo

**Marimo** is a reactive Python notebook framework where:
- Notebooks are stored as pure Python files (`.py`), not JSON
- Cells automatically re-execute when dependencies change (reactive dataflow)
- Notebooks can be run as scripts, web apps, or compiled to static HTML
- Code and outputs are tightly coupled, making them reproducible

This project leverages marimo's ability to:
1. Write content as interactive notebooks during development
2. Execute notebooks programmatically to capture outputs
3. Export the results as beautiful static HTML pages
4. Maintain the entire website as version-controlled Python code

## Codebase Structure

### Root Folders

- **`pages/`** - Marimo notebook files that become website pages
  - Each `.py` file is a marimo notebook
  - `home.py` is special: it's the entry point that builds the entire site
  - Uses `page_()` function convention to expose notebooks for building

- **`src/here/`** - Core library for the build system
  - Imported as `from here import ...` in notebooks (the pun: "from here import stuff")
  - Defines the `Embed` class for notebook execution and caching
  - Provides utilities like `me()`, `asset()`, path constants
  - Manages the execution → state → HTML rendering pipeline

- **`markup/`** - Non-Python content files
  - Jinja2 templates (`template.jinja`)
  - Markdown files for inclusion in notebooks
  - Typst files for document generation

- **`assets/`** - Static assets
  - CSS files (`style.css`, `code_highlighting.css`)
  - JavaScript (custom web components like carousel)
  - Fonts, images, logos

- **`web/`** - Generated output (git-ignored)
  - Final static HTML files
  - Copied assets
  - Ready to deploy

## The "here" Module

The `src/here/` module is the heart of the build system. The name is a deliberate pun: notebooks start with `from here import ...`, meaning "from this codebase, import utilities".

### Key API Components

**Core Classes:**
- `Embed` - Wraps a marimo notebook for execution and rendering
  - Constructor: `Embed(path, app, title, children=[], url=None, include=[])`
  - `._execute_notebook()` - Executes and caches notebook state (cached with `cachier`)
  - `._execute_all()` - Execute this notebook + all children recursively
  - `._execute_children()` - Execute only children (useful for custom home page rendering)

- `NotebookState` - Intermediate representation of executed notebook
  - Contains: title, url, code, outputs, python content
  - `.render(template_string, home_page_url="/", is_home=False)` - Render to HTML

- `MarimoPage` - Final HTML page ready to write
  - Contains: url, html_content

**Utilities:**
- `me()` - Returns personal info as polars DataFrame
- `asset(relative_path)` - Load PDF/media assets with fallback handling
- Path constants: `PATH_WEB`, `PATH_PAGES`, `PATH_ASSETS`, `PATH_MARKUP`

### Design Principles

- **Small surface area** - Minimal public API, everything you need and nothing more
- **Separation of concerns** - Execution (cached) vs rendering (not cached)
- **Composability** - Notebooks can be nested as trees (children)

## Build Process

### Execution Flow

1. **Entry point**: `mise run build` → executes `pages/home.py`

2. **home.py orchestration**:
   ```python
   root = page_()  # Creates Embed tree with all children
   
   # Execute all children (cached)
   for state in root._execute_children():
       html = template.render(state, is_home=False)
       write(state.url, html)
   
   # Execute and render home page specially
   home_state = root._execute_notebook(...)
   html = template.render(home_state, is_home=True)
   write("index.html", html)
   ```

3. **Caching strategy** (using `cachier`):
   - `Embed._execute_notebook(python_content, hash)` is cached to `.cache/`
   - Cache key = notebook content hash
   - Changing template doesn't invalidate cache (only re-renders)
   - Changing notebook code invalidates cache (re-executes)
   - Returns `NotebookState` object (intermediate representation)

4. **Rendering**:
   - Templates loaded via Jinja2 `FileSystemLoader`
   - Template receives `NotebookState` attributes + `is_home` flag
   - Different navbar for home (`is_home=True`) vs other pages

### mise.toml Tasks

- **`mise run sync`** - Sync Python dependencies (not frequently updated)
- **`mise run copy-assets`** - Copy `assets/` to `web/assets/`
- **`mise run build`** - Execute `pages/home.py` to generate all HTML
- **Default workflow**: `mise run build` handles everything

## Other Technologies

### Typst
- Modern markup language for creating documents (alternative to LaTeX)
- Used for generating PDFs and formatted content
- Files in `markup/*.typst` compiled and embedded in notebooks

### Python Libraries

**Data & Visualization:**
- **polars** - Fast DataFrame library (preferred over pandas)
- **altair** - Declarative visualization library (Vega-Lite based)

**Content Processing:**
- **pygments** - Syntax highlighting for code blocks
- **lzstring** - Compress Python code for marimo.app links
- **jinja2** - Template engine for HTML generation

**Notebook Infrastructure:**
- **marimo** - The notebook framework itself
- **cachier** - Persistent caching with file backend

## Coding Style

### Principles

1. **Concision over verbosity**
   - Prefer short, clear code over lengthy explanations
   - Use functional patterns where appropriate
   - One-liners are fine if readable

2. **Assertions over error catching**
   ```python
   # Good
   assert file_key is not None
   assert len(code) == len(outputs)
   
   # Avoid
   try:
       if file_key is None:
           raise ValueError(...)
   except ValueError:
       ...
   ```

3. **Continuous refactoring**
   - Always revisit code to improve clarity
   - Question: "Can this be simpler?"
   - Remove abstractions that don't pull their weight
   - Small API surface area is a feature

4. **Comments for "why", not "what"**
   - Code should be self-documenting
   - Comments explain rationale: `# This is when using a setup cell`
   - TODO comments are encouraged: `# TODO: refactor (ugly)`

### Patterns

- Use `Path` objects, not string concatenation
- Prefer comprehensions over loops where clear
- Type hints for public API, optional for internal code
- Use `_private` prefix for internal methods

## TODO.md

The `TODO.md` file exists but is **rarely up to date**. Don't trust it blindly:
- May contain outdated tasks
- May not reflect current priorities
- Can be useful for brainstorming ideas
- Better to ask the human for current priorities

When working on the project:
1. Check `TODO.md` for context, not gospel
2. Confirm tasks with the human before implementing
3. Update `TODO.md` if you make significant changes (but don't rely on it)

## Working with Agents

When AI agents work on this project:

**Do:**
- Ask questions when unclear (better than assumptions)
- Read the codebase before making changes
- Check if similar functionality already exists
- Look for opportunities to simplify, not just add features
- Test with `mise run build` after changes
- Clear cache (`rm -rf .cache`) when changing `NotebookState` structure

**Don't:**
- Add abstractions without clear benefits
- Catch errors that should be assertions
- Create redundant utilities
- Assume `TODO.md` is current
- Modify templates without understanding the rendering flow
- Add dependencies without asking

The project values **simplicity, clarity, and maintainability** over feature richness.
