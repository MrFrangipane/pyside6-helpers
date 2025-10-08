from typing import TypeVar, Generic, Any

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget


T = TypeVar("T")


class AnnotatedFormWidget(QWidget, Generic[T]):

    valueChanged = Signal(object, str)

    def __init__(self, dataclass_instance: T, parent=None):
        super().__init__(parent)
        self._dataclass_instance: T = dataclass_instance

    def value(self) -> T:
        return self._dataclass_instance

    @Slot()
    def set_value(self, name: str, value: Any):
        setattr(self._dataclass_instance, name, value)
        self.valueChanged.emit(self._dataclass_instance, name)
