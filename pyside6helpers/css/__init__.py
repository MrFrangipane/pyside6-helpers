from importlib import resources

from PySide6.QtWidgets import QWidget, QApplication


def load_onto(target: QWidget | QApplication, theme_filename: str = "dark-desktop.qss"):
    resource_path = resources.files("pyside6helpers.resources").joinpath(theme_filename)
    with resources.as_file(resource_path) as p:
        with open(p, "r") as f:
            target.setStyleSheet(f.read())
