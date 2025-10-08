from typing import Any, Tuple

from pyside6helpers.annotated_form.type_enum import WidgetTypeEnum


class WidgetAnnotation:
    def __init__(self, type_enum: WidgetTypeEnum, label: str, range_: Tuple[Any, Any] | None = None, group: str | None = None, values: list[Any] = None):
        self.type = type_enum
        self.label = label
        self.range = range_
        self.group = group
        self.values = values if values is not None else []
