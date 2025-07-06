from typing import get_type_hints, Any, Annotated, get_origin, get_args

from PySide6.QtWidgets import QWidget, QFormLayout, QLabel, QSlider

from pyside6helpers.annotated_form.types import WidgetAnnotation, WidgetTypeEnum
from pyside6helpers.slider import Slider


class AnnotatedFormWidgetMaker:

    def __init__(self, dataclass_instance):
        self._dataclass_instance = dataclass_instance
        self._layout: QFormLayout | None = None

    def make_widget(self) -> QWidget:
        items = get_type_hints(self._dataclass_instance, include_extras=True).items()

        new_widget = QWidget()
        self._layout = QFormLayout(new_widget)

        for name, type_hint in items:
            self._make_widget(name, type_hint)

        return new_widget

    def _make_widget(self, name:str, type_hint: Any) -> None:
        if get_origin(type_hint) != Annotated:
            raise ValueError(f"Invalid widget annotation for {type_hint}")

        type_, annotation = get_args(type_hint)
        if not isinstance(annotation, WidgetAnnotation):
            raise ValueError(f"Invalid widget annotation for {type_hint}")

        annotation: WidgetAnnotation = annotation
        if annotation.type == WidgetTypeEnum.Slider:
            self._layout.addRow(
                QLabel(annotation.label),
                Slider(
                    minimum=annotation.range[0],
                    maximum=annotation.range[1],
                    value=getattr(self._dataclass_instance, name)
                )
            )


if __name__ == '__main__':
    import sys
    from dataclasses import dataclass

    from PySide6.QtWidgets import QApplication, QWidget

    from pyside6helpers.annotated_form import types


    @dataclass
    class DemoAnnotated:
        value_a: types.IntegerSliderType("Value A", (-100, 100))
        value_b: types.IntegerSliderType("Value that is B", (0, 100))
        value_c: types.IntegerSliderType("C", (-100, 0))

    instance = DemoAnnotated(
        value_a=34,
        value_b=56,
        value_c=78
    )

    app = QApplication(sys.argv)
    widget = AnnotatedFormWidgetMaker(instance).make_widget()
    widget.show()
    app.exec()
