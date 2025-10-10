from typing import Any

from PySide6.QtCore import Qt

from pyside6helpers.annotated_form.type_enum import WidgetTypeEnum


class WidgetAnnotation:
    def __init__(self, type_enum: WidgetTypeEnum, label: str, range_: tuple[Any, Any] | None = None, group: str | None = None, values: list[Any] = None, orientation: int | None = None):
        self.type = type_enum
        self.label = label
        self.range = range_
        self.group = group
        self.values = values if values is not None else []
        self.orientation = orientation if orientation is not None else Qt.Vertical
