from typing import List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy


def make_group(title: str, widgets: List[QWidget], orientation=Qt.Vertical, tooltip: str = None, fixed_width: int = None, fixed_height: int = None):
    """
    Creates a QGroupBox with given widgets, title and orientation
    """
    group = QGroupBox(title)
    group.setToolTip(tooltip)
    layout = QVBoxLayout(group) if orientation == Qt.Vertical else QHBoxLayout(group)

    for widget in widgets:
        layout.addWidget(widget)

    if fixed_width is not None:
        group.setFixedWidth(fixed_width)

    if fixed_height is not None:
        group.setFixedHeight(fixed_height)

    return group


def make_group_grid(title: str, widgets: List[List[QWidget]], stretch_last_column=False):
    """
    Creates a QGroupBox with given widgets and title
    Layout is QGridLayout
    """
    group = QGroupBox(title)
    layout = QGridLayout(group)

    for row, widget_row in enumerate(widgets):
        for column, widget in enumerate(widget_row):
            layout.addWidget(widget, row, column)

    if stretch_last_column:
        layout.setColumnStretch(len(widgets[0]) - 1, 1)

    return group
