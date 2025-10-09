from typing import get_type_hints, Any, Annotated, get_origin, get_args, Type, Tuple

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFormLayout, QLabel, QPushButton, QCheckBox, QGroupBox, QVBoxLayout, \
    QRadioButton, QHBoxLayout

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

        for field_name, type_hint in items:
            self._make_widget(field_name, type_hint)

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

    def _make_widget(self, field_name:str, type_hint: Any) -> None:
        if get_origin(type_hint) != Annotated:
            raise ValueError(f"Invalid widget annotation for {type_hint}")

        type_, annotation = get_args(type_hint)
        if not isinstance(annotation, WidgetAnnotation):
            raise ValueError(f"Invalid widget annotation for {type_hint}")


        value = getattr(self._dataclass_instance, field_name)
        annotation: WidgetAnnotation = annotation  # type hinting only?

        if annotation.type == WidgetTypeEnum.NoWidget:
            return

        elif annotation.type == WidgetTypeEnum.Slider:
            self._add_row(
                field_name,
                QLabel(annotation.label),
                Slider(
                    minimum=annotation.range[0],
                    maximum=annotation.range[1],
                    value=value,
                    on_value_changed=lambda value: self._new_widget.set_value(field_name, value)
                ),
                annotation.group
            )

        elif annotation.type == WidgetTypeEnum.Button:
            button = QPushButton(annotation.label)
            button.pressed.connect(lambda: self._new_widget.set_value(field_name, annotation.range[1]))
            button.released.connect(lambda: self._new_widget.set_value(field_name, annotation.range[0]))
            self._add_row(field_name, QLabel(), button, annotation.group)

        elif annotation.type == WidgetTypeEnum.Radio:
            widget = QWidget()
            layout = QVBoxLayout(widget) if annotation.orientation == Qt.Vertical else QHBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            for enum_name, enum_value in annotation.values:
                radio = QRadioButton(enum_name)
                radio.setChecked(value == enum_value)
                # Python lambda closure issue resolved using default parameters
                radio.clicked.connect(lambda checked, fn=field_name, v=enum_value: self._handle_radio_click(fn, enum_name, v))
                layout.addWidget(radio)

            if annotation.orientation == Qt.Horizontal:
                layout.addStretch()

            self._add_row(field_name, QLabel(annotation.label), widget, annotation.group)

        else:
            checkbox = QCheckBox(annotation.label)
            checkbox.setChecked(value)
            checkbox.checkStateChanged.connect(lambda state: self._new_widget.set_value(field_name, annotation.range[1] if state == Qt.CheckState.Checked else annotation.range[0]))
            self._add_row(field_name, None, checkbox, annotation.group)

    def _add_row(self, field_name: str, label: QLabel | None, widget: QWidget, group: str):
        self._new_widget.widgets[field_name] = widget
        group_names = [group_name for group_name, _ in self._widgets]

        if not group:
            self._widgets.append((group, [(label, widget)]))

        else:
            if group not in group_names:
                self._widgets.append((group, []))
                group_names = [group_name for group_name, _ in self._widgets]

            self._widgets[group_names.index(group)][1].append((label, widget))

    def _handle_radio_click(self, field_name: str, name: str, value: Any):
        self._new_widget.set_value(field_name, value)

if __name__ == '__main__':
    import sys
    from dataclasses import dataclass
    from enum import Enum

    from PySide6.QtWidgets import QApplication, QWidget

    from pyside6helpers.annotated_form import types


    class RadioEnum(Enum):
        Un = 1
        Deux = "Deux"
        Trois = 3.0


    @dataclass
    class DemoAnnotated:
        value_a: types.IntegerSliderType("Value A", (-100, 100), group="Group A")
        value_b: types.IntegerSliderType("Value that is B", (0, 100))
        value_c: types.IntegerSliderType("C", (-100, 0), group="Group CD")
        value_d: types.IntegerSliderType("D", (-100, 0), group="Group CD")
        value_e: types.RadioEnumType("Enum", RadioEnum)

    instance = DemoAnnotated(
        value_a=34,
        value_b=56,
        value_c=78,
        value_d=90,
        value_e=RadioEnum.Trois,
    )

    def changed(value: DemoAnnotated, sender: str):
        print(">>", sender, value)

    app = QApplication(sys.argv)
    widget_ = AnnotatedFormWidgetMaker(instance).make_widget()
    widget_.valueChanged.connect(changed)
    widget_.show()
    app.exec()
