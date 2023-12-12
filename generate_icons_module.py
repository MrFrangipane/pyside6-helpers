"""Generate a python module for PySide6 with all icons"""
import os.path
import logging
from glob import glob

from pyside6helpers.resources import make_resource_path


logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger("Icon Generator")


_MODULE = """from functools import cache

from PySide6.QtGui import QIcon
from pyside6helpers.resources import make_resource_path
"""


_TEMPLATE = """

@cache
def {name}():
    return QIcon(make_resource_path("icons/{name}.png"))
"""


_logger.info(f"reset module")


module = _MODULE
for icon in glob(make_resource_path("icons/*.png")):
    name = os.path.basename(icon)
    name = os.path.splitext(name)[0]
    name = name.replace('-', '_')

    _logger.info(f"added {name}")

    module += _TEMPLATE.format(name=name)


module_filepath = "pyside6helpers/icons.py"
with open(module_filepath, "w") as module_file:
    module_file.write(module)

_logger.info(f"wrote python module {os.path.abspath(module_filepath)}")
