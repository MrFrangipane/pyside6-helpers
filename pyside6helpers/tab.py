from PySide6.QtWidgets import (QTabWidget, QWidget)


def make_tabs(widgets: dict[str, QWidget]):
    tabs = QTabWidget()
    for caption, widget in widgets.items():
        tabs.addTab(widget, caption)

    return tabs
