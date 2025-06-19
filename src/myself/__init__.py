import polars as pl
from datetime import date
from pathlib import Path
import shutil
from IPython.display import IFrame, SVG, Audio

pl.Config.set_tbl_hide_column_data_types(True)


def age(birth):
    today = date.today()
    years = today.year - birth.year
    if today.month < birth.month or (
        today.month == birth.month and today.day < birth.day
    ):
        years -= 1
    return years


birth = date(year=2003, month=8, day=18)

info = pl.DataFrame(
    {
        "name": ["Antonin"],
        "alias": ["@rambip"],
        "age": [age(birth)],
        "current_education": ["Télécom Paris (year break)"],
    }
)

PROJECTS = Path(__file__).parent.parent.parent.parent
ASSETS = Path(__file__).parent.parent.parent / "assets"


def asset(relative_path):
    path = PROJECTS / relative_path
    extension = path.name.split(".")[-1]
    identifier = (
        path.name.split(".")[0].__hash__() if "." in path.name else path.name.__hash__()
    )
    if "." in path.name:
        identifier = str(identifier) + "." + extension
    else:
        identifier = str(identifier)
    shutil.copy(path, ASSETS / identifier)
    path_for_website = f"assets/{identifier}"

    if extension == "pdf":
        return IFrame(path_for_website, 700, 1000)

    if extension == "mp3":
        return Audio(path_for_website)

    if extension == "svg":
        with open(path) as f:
            return SVG(f.read())
