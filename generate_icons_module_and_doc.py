"""Generate a python module for PySide6 with all icons

This is ugly as it gets"""
import os.path
import logging
from glob import glob

from pyside6helpers import resources


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger("Icon Generator")


_DOC_COLUMN_COUNT = 4
_MODULE = """from functools import cache

from PySide6.QtGui import QIcon, QPixmap, QColor, Qt

from pyside6helpers.resources import make_path


def _make_color(filepath, color: QColor):
    pixmap = QPixmap(filepath)
    mask = pixmap.mask()
    white_pixmap = QPixmap(pixmap.size())
    white_pixmap.fill(color)
    white_pixmap.setMask(mask)
    return white_pixmap
"""
_FUNCTION_TEMPLATE = """

@cache
def {name_function}(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/{name_file}.png"), color))
"""
_DOC = """# Icons

Provided icons requires you state the follwing message to your users

````
Icons made by https://www.freepik.com (https://www.flaticon.com)
````

Code example

````python
from pyside6helpers import icons

icon_reload = icons.refresh()  # provides a QIcon for refresh.png
````

"""
_DOC += ("| Icon | Name " * _DOC_COLUMN_COUNT) + "|\n"
_DOC += ("|------|------" * _DOC_COLUMN_COUNT) + "|\n"
_DOC_LINE_TEMPLATE = "| ![](pyside6helpers/resources/icons/{name_file}.png) | `{name_function}()` "


_logger.info(f"reset module")
_logger.info(f"reset doc")


module = _MODULE
doc = _DOC
column = 0
doc_line = ""
icons = glob(resources.make_path("icons/*.png"))
for index, icon in enumerate(icons):
    name_file = os.path.basename(icon)
    name_file = os.path.splitext(name_file)[0]

    name_function = name_file.replace('-', '_')

    _logger.info(f"added {name_file} column {column}")

    #
    # Module
    module += _FUNCTION_TEMPLATE.format(name_function=name_function, name_file=name_file)

    #
    # Doc
    if column == 0:
        doc_line = _DOC_LINE_TEMPLATE.format(name_function=name_function, name_file=name_file)
        column += 1

    elif column < _DOC_COLUMN_COUNT:
        doc_line += _DOC_LINE_TEMPLATE.format(name_function=name_function, name_file=name_file)
        column += 1

    if column == _DOC_COLUMN_COUNT:
        column = 0
        doc_line += "|\n"
        doc += doc_line
    elif index == len(icons) - 1:
        doc += doc_line

if column < _DOC_COLUMN_COUNT:
    doc += ("|   |   " * (_DOC_COLUMN_COUNT - column)) + "|\n"


module_filepath = "pyside6helpers/icons.py"
with open(module_filepath, "w") as module_file:
    module_file.write(module)

_logger.info(f"wrote python module {os.path.abspath(module_filepath)}")

doc_filepath = "icons.md"
with open(doc_filepath, "w") as doc_file:
    doc_file.write(doc)

_logger.info(f"wrote doc file {os.path.abspath(doc_filepath)}")
