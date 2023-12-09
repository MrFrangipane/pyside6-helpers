from typing import List

from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide6.QtCore import Qt


def make_group(title: str, widgets: List[QWidget], orientation=Qt.Vertical):
    """
    Creates a QGroupBox with given widgets, title and orientation
    """
    group = QGroupBox(title)
    layout = QVBoxLayout(group) if orientation == Qt.Vertical else QHBoxLayout(group)

    for widget in widgets:
        layout.addWidget(widget)

    return group


def make_group_grid(title: str, widgets: List[List[QWidget]]):
    """
    Creates a QGroupBox with given widgets and title
    Layout is QGridLayout
    """
    group = QGroupBox(title)
    layout = QGridLayout(group)

    for row, widget_row in enumerate(widgets):
        for column, widget in enumerate(widget_row):
            layout.addWidget(widget, row, column)

    return group
