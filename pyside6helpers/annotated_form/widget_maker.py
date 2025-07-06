from typing import get_type_hints, Any, Annotated, get_origin, get_args, Type

from PySide6.QtWidgets import QFormLayout, QLabel

from pyside6helpers.annotated_form.form_widget import AnnotatedFormWidget
from pyside6helpers.annotated_form.types import WidgetAnnotation, WidgetTypeEnum
from pyside6helpers.slider import Slider


class AnnotatedFormWidgetMaker:

    def __init__(self, dataclass_instance: Any):
        self._dataclass_instance = dataclass_instance
        self._layout: QFormLayout | None = None
        self._new_widget: AnnotatedFormWidget[Type[Any]] | None = None

    def make_widget(self) -> AnnotatedFormWidget[Type[Any]]:
        items = get_type_hints(self._dataclass_instance, include_extras=True).items()

        self._new_widget = AnnotatedFormWidget[type(self._dataclass_instance)](
            dataclass_instance=self._dataclass_instance
        )
        self._layout = QFormLayout(self._new_widget)

        for name, type_hint in items:
            self._make_widget(name, type_hint)

        return self._new_widget

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
                    value=getattr(self._dataclass_instance, name),
                    on_value_changed=lambda value: self._new_widget.set_value(name, value)
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

    def changed(value: DemoAnnotated):
        print(value)

    app = QApplication(sys.argv)
    widget = AnnotatedFormWidgetMaker(instance).make_widget()
    widget.valueChanged.connect(changed)
    widget.show()
    app.exec()
