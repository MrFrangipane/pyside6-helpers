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
    NoWidget = 0
    Button = 1
    CheckBox = 2
    Slider = 3


class WidgetAnnotation:
    def __init__(self, type_enum: WidgetTypeEnum, label: str, range_: Tuple[Any, Any], group: str):
        self.type = type_enum
        self.label = label
        self.range = range_
        self.group = group


def ButtonType(label: str, range_: Tuple[int, int], group: str = None):
    return Annotated[int, WidgetAnnotation(
        type_enum=WidgetTypeEnum.Button,
        label=label,
        range_=range_,
        group=group
    )]


def CheckBoxType(label: str, range_: Tuple[int, int], group: str = None):
    return Annotated[bool, WidgetAnnotation(
        type_enum=WidgetTypeEnum.CheckBox,
        label=label,
        range_=range_,
        group=group
    )]


def IntegerSliderType(label: str, range_: Tuple[int, int], group: str = None):
    return Annotated[int, WidgetAnnotation(
        type_enum=WidgetTypeEnum.Slider,
        label=label,
        range_=range_,
        group=group
    )]

def NoWidgetType():
    return Annotated[int, WidgetAnnotation(
        type_enum=WidgetTypeEnum.NoWidget,
        label="",
        range_=(0, 0),
        group=None
    )]
