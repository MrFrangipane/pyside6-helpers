from typing import get_type_hints, Any, Annotated, get_origin, get_args, Type, Tuple

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFormLayout, QLabel, QPushButton, QCheckBox, QGroupBox

from pyside6helpers.annotated_form.form_widget import AnnotatedFormWidget
from pyside6helpers.annotated_form.types import WidgetAnnotation, WidgetTypeEnum
from pyside6helpers.slider import Slider


class AnnotatedFormWidgetMaker:

    def __init__(self, dataclass_instance: Any):
        self._dataclass_instance = dataclass_instance
        self._layout: QFormLayout | None = None
        self._new_widget: AnnotatedFormWidget[Type[Any]] | None = None
        self._widgets: list[Tuple[str, Tuple[QWidget, QWidget]]] = []

    def make_widget(self) -> AnnotatedFormWidget[Type[Any]]:
        items = get_type_hints(self._dataclass_instance, include_extras=True).items()

        self._new_widget = AnnotatedFormWidget[type(self._dataclass_instance)](
            dataclass_instance=self._dataclass_instance
        )
        self._layout = QFormLayout(self._new_widget)

        for name, type_hint in items:
            self._make_widget(name, type_hint)

        from pprint import pprint
        pprint(self._widgets)

        for group_name, widgets in self._widgets:
            if not group_name:
                for label, widget in widgets:
                    self._layout.addRow(label, widget)

            else:
                group_box = QGroupBox(group_name)
                layout = QFormLayout(group_box)
                for label, widget in widgets:
                    layout.addRow(label, widget)
                self._layout.addRow(group_box)

        return self._new_widget

    def _make_widget(self, name:str, type_hint: Any) -> None:
        if get_origin(type_hint) != Annotated:
            raise ValueError(f"Invalid widget annotation for {type_hint}")

        type_, annotation = get_args(type_hint)
        if not isinstance(annotation, WidgetAnnotation):
            raise ValueError(f"Invalid widget annotation for {type_hint}")

        annotation: WidgetAnnotation = annotation
        if annotation.type == WidgetTypeEnum.NoWidget:
            return

        elif annotation.type == WidgetTypeEnum.Slider:
            self._add_row(
                QLabel(annotation.label),
                Slider(
                    minimum=annotation.range[0],
                    maximum=annotation.range[1],
                    value=getattr(self._dataclass_instance, name),
                    on_value_changed=lambda value: self._new_widget.set_value(name, value)
                ),
                annotation.group
            )

        elif annotation.type == WidgetTypeEnum.Button:
            button = QPushButton(annotation.label)
            button.pressed.connect(lambda: self._new_widget.set_value(name, annotation.range[1]))
            button.released.connect(lambda: self._new_widget.set_value(name, annotation.range[0]))
            self._add_row(QLabel(), button, annotation.group)

        else:
            checkbox = QCheckBox(annotation.label)
            checkbox.checkStateChanged.connect(lambda state: self._new_widget.set_value(name, annotation.range[1] if state == Qt.CheckState.Checked else annotation.range[0]))
            self._add_row(QLabel(), checkbox, annotation.group)

    def _add_row(self, label: QLabel, widget: QWidget, group: str):
        group_names = [group_name for group_name, _ in self._widgets]

        if not group:
            self._widgets.append((group, [(label, widget)]))

        else:
            if group not in group_names:
                self._widgets.append((group, []))
                group_names = [group_name for group_name, _ in self._widgets]

            self._widgets[group_names.index(group)][1].append((label, widget))


if __name__ == '__main__':
    import sys
    from dataclasses import dataclass

    from PySide6.QtWidgets import QApplication, QWidget

    from pyside6helpers.annotated_form import types


    @dataclass
    class DemoAnnotated:
        value_a: types.IntegerSliderType("Value A", (-100, 100), group="Group A")
        value_b: types.IntegerSliderType("Value that is B", (0, 100))
        value_c: types.IntegerSliderType("C", (-100, 0), group="Group CD")
        value_d: types.IntegerSliderType("D", (-100, 0), group="Group CD")

    instance = DemoAnnotated(
        value_a=34,
        value_b=56,
        value_c=78,
        value_d=90
    )

    def changed(value: DemoAnnotated, sender: str):
        print(sender, value)

    app = QApplication(sys.argv)
    widget_ = AnnotatedFormWidgetMaker(instance).make_widget()
    widget_.valueChanged.connect(changed)
    widget_.show()
    app.exec()
