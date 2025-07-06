__all__ = [
    "ButtonType",
    "CheckBoxType",
    'IntegerSliderType',
    'WidgetAnnotation',
    'WidgetTypeEnum',
]
from enum import Enum
from typing import Annotated, Tuple, Any


class WidgetTypeEnum(Enum):
    Button = 1
    CheckBox = 2
    Slider = 0


class WidgetAnnotation:
    def __init__(self, type_enum: WidgetTypeEnum, label: str, range_: Tuple[Any, Any]):
        self.type = type_enum
        self.label = label
        self.range = range_


def ButtonType(label: str, range_: Tuple[int, int]):
    return Annotated[int, WidgetAnnotation(
        type_enum=WidgetTypeEnum.Button,
        label=label,
        range_=range_
    )]


def CheckBoxType(label: str, range_: Tuple[int, int]):
    return Annotated[bool, WidgetAnnotation(
        type_enum=WidgetTypeEnum.CheckBox,
        label=label,
        range_=range_
    )]


def IntegerSliderType(label: str, range_: Tuple[int, int]):
    return Annotated[int, WidgetAnnotation(
        type_enum=WidgetTypeEnum.Slider,
        label=label,
        range_=range_
    )]
