__all__ = [
    'IntegerSliderType',
    'WidgetAnnotation',
    'WidgetTypeEnum',
]
from enum import Enum
from typing import Annotated, Tuple, Any


class WidgetTypeEnum(Enum):
    Slider = 0


class WidgetAnnotation:
    def __init__(self, type_enum: WidgetTypeEnum, label: str, range_: Tuple[Any, Any]):
        self.type = type_enum
        self.label = label
        self.range = range_


def IntegerSliderType(label: str, range_: Tuple[int, int]):
    return Annotated[int, WidgetAnnotation(
        type_enum=WidgetTypeEnum.Slider,
        label=label,
        range_=range_
    )]
