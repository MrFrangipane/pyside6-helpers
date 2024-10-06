from PySide6.QtWidgets import QWidget

from pyside6helpers import resources


def load_onto(q_widget: QWidget):
    filepath = resources.make_path("dark.qss")
    print(filepath)
    with open(filepath, "r") as stylesheet_file:
        q_widget.setStyleSheet(stylesheet_file.read())
