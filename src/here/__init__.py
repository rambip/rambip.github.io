import base64
import datetime
import os
import shutil
from io import StringIO
from pathlib import Path
from typing import Iterable, Sequence

import lzstring
import marimo
import polars as pl
from cachier import cachier
from dotenv import load_dotenv
from jinja2 import BaseLoader, Environment
from marimo._ast.models import CellData
from marimo._runtime.watch._file import FileState
from marimo._server.file_router import AppFileRouter
from marimo._utils.marimo_path import MarimoPath
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

load_dotenv()
PATH_WEB = Path(__file__).parent.parent.parent / "web"
PATH_PAGES = Path(__file__).parent.parent.parent / "pages"
PATH_ASSETS = Path(__file__).parent.parent.parent / "assets"
PATH_TEMPLATES = Path(__file__).parent / "templates"
if "PROJECT_DIR" in os.environ:
    PROJECTS = Path(os.environ["PROJECT_DIR"])
else:
    PROJECTS = None

# Home page URL constant
HOME_PAGE_URL = "/index.html"

with open(Path(__file__).parent / "templates" / "main.html") as f:
    HTML_TEMPLATE = f.read()


def compute_age(birth_date) -> int:
    today = datetime.date.today()
    years = today.year - birth_date.year
    if today.month < birth_date.month or (
        today.month == birth_date.month and today.day < birth_date.day
    ):
        years -= 1
    return years


def me():
    birth_date = datetime.date(2003, 8, 18)
    age = compute_age(birth_date)
    name = "Antonin"
    alias = "rambip"
    return pl.DataFrame([{"age": age, "name": name, "alias": alias}])


class SimplifiedCellData:
    def __init__(self, cell: CellData):
        self.code = cell.code
        self.config = cell.config


def get_cells(path: Path) -> Sequence[SimplifiedCellData]:
    # Create a file router
    m_path = MarimoPath(path)
    file_router = AppFileRouter.from_filename(m_path)
    file_key = file_router.get_unique_file_key()
    assert file_key is not None

    # Use the file path directly for configuration
    # config = get_default_config_manager(current_path=str(path))
    return [
        SimplifiedCellData(c)
        for c in file_router.get_file_manager(file_key).app.cell_manager.cell_data()
    ]


# if you make changes to this, you need to clear the cachier cache
class MarimoPage:
    def __init__(self, url, html_content):
        self.url = url
        self.html_content = html_content


class Embed:
    def __init__(
        self,
        path,
        app: marimo.App,
        link_name: str,
        children: Sequence["Embed"] = [],
        url=None,
        include: Sequence[FileState] = [],
    ):
        self.path = Path(path)
        self.app = app
        self.children = tuple(children)
        if url is None:
            self.url = f"{self.path.name}.html"
        else:
            self.url = url
        self.link_name = link_name
        self.cells = get_cells(path)
        self.includes = [f.read_text() for f in include]
        seed_code = StringIO()
        seed_code.write(
            "with app.setup(hide_code=True):\n    from pathlib import Path as _Path\n"
        )
        for i, f in enumerate(include):
            markup_path = str(f._value)
            content = f.read_text()

            seed_code.write(
                f"    _included_file_to_generate_{i} = _Path({repr(markup_path)})\n"
                f"    if not _included_file_to_generate_{i}.exists():\n"
                f"        _included_file_to_generate_{i}.parent.mkdir(exist_ok=True, parents=True)\n"
                f"        with open(_included_file_to_generate_{i}, 'w') as f:\n"
                f"            f.write({repr(content)})\n"
                "\n"
            )
        with open(self.path, "r") as f:
            python_content = f.read()

        self.python_content = python_content.replace(
            "with app.setup(hide_code=True):", seed_code.getvalue()
        )

    def _repr_html_(self):
        return f'<a href="/{self.url}">{self.link_name}</a>'

    @cachier()
    def _build_html(
        self,
        python_content: str,
        _hash: int,
        template_string: str,
    ) -> MarimoPage:
        template = Environment(loader=BaseLoader()).from_string(template_string)
        print(f"building page {self.path.name}")
        content = f"dummy content of {self.path.name}"

        def repr_(x):
            if x is None:
                return None
            if hasattr(x, "_repr_html_"):
                return x._repr_html_()
            return repr(x)

        outputs = [repr_(x) for x in self.app.run({"IN_THE_MATRIX": True})[0]]
        lexer = PythonLexer()
        formater = HtmlFormatter()
        code = [
            highlight(c.code, lexer, formater)
            if not c.config.hide_code and not c.config.disabled
            else None
            for c in self.cells
        ]
        if len(code) != len(outputs):
            mismatch = len(code) - len(outputs)
            # this is when using a setup cell.
            # Marimo does not seem to provide an API to know if the cell is a setup-cell
            outputs = mismatch * [None] + outputs
            assert len(code) == len(outputs), (
                f"outputs is len {len(outputs)} and code is len {len(code)}"
            )
        content = list(zip(code, outputs))

        data_for_marimo = lzstring.LZString.compressToEncodedURIComponent(
            python_content
        )
        html_content = template.render(
            name=self.path.name,
            content=content,
            home_page_url=HOME_PAGE_URL,
            python_content_encoded=base64.b64encode(
                bytes(python_content, "utf-8")
            ).decode("utf-8"),
            python_filename=self.path.name,
            python_content_for_marimo=data_for_marimo,
        )
        return MarimoPage(self.url, html_content)

    def __hash__(self) -> int:
        return hash((self.python_content, self.children))

    def _build_(self) -> Iterable[MarimoPage]:
        for c in self.children:
            yield from c._build_()

        yield self._build_html(self.python_content, hash(self), HTML_TEMPLATE)


def asset(relative_path: str):
    target_path: Path = PATH_ASSETS / relative_path
    if not target_path.exists():
        if PROJECTS is None:
            return marimo.Html('<span style="color:orange">Can\'t access assets</span>')
        else:
            target_path.parent.mkdir(exist_ok=True)
            shutil.copy(PROJECTS / relative_path, target_path)
    extension = relative_path.split(".")[-1]
    assert extension == "pdf"
    if marimo.running_in_notebook():
        return marimo.pdf(target_path)
    return marimo.Html(f"<iframe src=/assets/{relative_path}></iframe>")
