__all__ = [
    'ButtonType',
    'CheckBoxType',
    'IntegerSliderType',
    'NoWidgetType',
    'RadioEnumType'
]
from enum import Enum
from typing import Annotated, Tuple, Type

from pyside6helpers.annotated_form.annotation import WidgetAnnotation
from pyside6helpers.annotated_form.type_enum import WidgetTypeEnum


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
    )]


def RadioEnumType(label: str, enum_type: Type[Enum], orientation: int = None, group: str = None):
    return Annotated[int, WidgetAnnotation(
        type_enum=WidgetTypeEnum.Radio,
        label=label,
        values=[(i.name, i) for i in enum_type],
        orientation=orientation,
        group=group
    )]
