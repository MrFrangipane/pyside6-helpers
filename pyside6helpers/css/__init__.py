from PySide6.QtWidgets import QWidget, QApplication

from pyside6helpers import resources


def load_onto(target: QWidget | QApplication, theme_filename: str = "dark.qss"):
    filepath = resources.make_path(theme_filename)
    with open(filepath, "r") as stylesheet_file:
        target.setStyleSheet(stylesheet_file.read())
