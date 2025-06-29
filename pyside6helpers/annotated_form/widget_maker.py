from typing import get_type_hints, Any

from PySide6.QtWidgets import QWidget, QFormLayout


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

    def _make_widget(self, name: str, type_hint: Any) -> None:
        print(name, type_hint)


if __name__ == '__main__':
    import sys
    from dataclasses import dataclass

    from PySide6.QtWidgets import QApplication, QWidget

    from pyside6helpers.annotated_form import types


    @dataclass
    class DemoAnnotated:
        value_a: types.IntegerSliderType("Value A", (-100, 100))

    instance = DemoAnnotated(
        value_a=34
    )

    app = QApplication(sys.argv)
    widget = AnnotatedFormWidgetMaker(instance).make_widget()
    widget.show()
    app.exec()
