"""Generate a python module for PySide6 with all icons"""
import os.path
import logging
from glob import glob

from pyside6helpers.resources import make_resource_path


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger("Icon Generator")


_MODULE = """from functools import cache

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from pyside6helpers.resources import make_resource_path


def _make_white(filepath):
    pixmap = QPixmap(filepath)
    mask = pixmap.mask()
    white_pixmap = QPixmap(pixmap.size())
    white_pixmap.fill(Qt.white)
    white_pixmap.setMask(mask)
    return white_pixmap
"""
_FUNCTION_TEMPLATE = """

@cache
def {name_function}() -> QIcon:
    return QIcon(_make_white(make_resource_path("icons/{name_file}.png")))
"""
_DOC = """# Icons

Provided icons requires you state the follwing message to your users

````
Icons made by https://www.freepik.com (https://www.flaticon.com)
````

````python
from pyside6helpers import icons

icon_reload = icons.refresh()
````

| Name         | Icon                                                 | 
|--------------|------------------------------------------------------|
"""
_DOC_LINE_TEMPLATE = "| `{name_function}()` | ![](pyside6helpers/resources/icons/{name_file}.png) |\n"


_logger.info(f"reset module")
_logger.info(f"reset doc")


module = _MODULE
doc = _DOC
for icon in glob(make_resource_path("icons/*.png")):
    name_file = os.path.basename(icon)
    name_file = os.path.splitext(name_file)[0]

    name_function = name_file.replace('-', '_')

    _logger.info(f"added {name_file}")

    module += _FUNCTION_TEMPLATE.format(name_function=name_function, name_file=name_file)
    doc += _DOC_LINE_TEMPLATE.format(name_function=name_function, name_file=name_file)


module_filepath = "pyside6helpers/icons.py"
with open(module_filepath, "w") as module_file:
    module_file.write(module)

_logger.info(f"wrote python module {os.path.abspath(module_filepath)}")

doc_filepath = "icons.md"
with open(doc_filepath, "w") as doc_file:
    doc_file.write(doc)

_logger.info(f"wrote doc file {os.path.abspath(doc_filepath)}")
