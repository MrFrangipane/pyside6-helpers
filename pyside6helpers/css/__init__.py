import os.path

from PySide6.QtWidgets import QWidget


_HERE = os.path.dirname(__file__)


def _make_resource_filepath(filename):
    return os.path.join(os.path.dirname(_HERE), "resources", filename)


def load_onto(q_widget: QWidget, filepath=None):
    if filepath is None:
        filepath = _make_resource_filepath("dark.qss")

    with open(filepath, "r") as stylesheet_file:
        q_widget.setStyleSheet(stylesheet_file.read())
