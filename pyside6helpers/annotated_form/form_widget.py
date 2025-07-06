from typing import TypeVar, Generic

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget


T = TypeVar("T")


class FormWidget(QWidget, Generic[T]):

    valueChanged = Signal(T)
    savePressed = Signal(T)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._dataclass: T | None = None

    def value(self) -> T:
        return self._dataclass
