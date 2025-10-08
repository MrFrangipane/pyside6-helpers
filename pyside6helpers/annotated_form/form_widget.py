from dataclasses import fields
from typing import TypeVar, Generic, Any

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from pyside6helpers.slider import Slider

T = TypeVar("T")


class AnnotatedFormWidget(QWidget, Generic[T]):

    valueChanged = Signal(object, str)

    def __init__(self, dataclass_instance: T, parent=None):
        super().__init__(parent)
        self._dataclass_instance: T = dataclass_instance
        self.widgets: dict[str: QWidget] = {}

    def value(self) -> T:
        return self._dataclass_instance

    @Slot()
    def set_value(self, name: str, value: Any):
        setattr(self._dataclass_instance, name, value)
        self.valueChanged.emit(self._dataclass_instance, name)

    @Slot()
    def set_dataclass_instance(self, dataclass_instance: T):
        self._dataclass_instance = dataclass_instance
        for field in fields(self._dataclass_instance):
            widget = self.widgets.get(field.name)
            if widget is not None:

                widget.blockSignals(True)

                if isinstance(widget, Slider):
                    widget.setValue(getattr(self._dataclass_instance, field.name))

                widget.blockSignals(False)
