from typing import Callable

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider

from pyside6helpers.label_editable import LabelEditable


class Slider(QWidget):  # FIXME autocompletion ?
    """
    Thin wrapper for a QSlider that shows its value and allows the edition of its name (emits editingCommitted)
    """
    editingCommitted = Signal(str)

    def __init__(self, name=None, is_vertical=False, minimum=0, maximum=0, value=0, single_step=1, on_value_changed: Callable=None, label_editable=False, parent=None):
        QWidget.__init__(self, parent)

        self._name_widget = None

        value = min(max(minimum, value), maximum)

        if is_vertical:
            self.slider = QSlider(Qt.Vertical)
            layout = QVBoxLayout(self)
        else:
            self.slider = QSlider(Qt.Horizontal)
            layout = QHBoxLayout(self)

        self.slider.setSingleStep(single_step)
        self.slider.setMinimum(minimum)
        self.slider.setMaximum(maximum)
        self.slider.setValue(value)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self._label_minimum = minimum
        self._label_maximum = maximum

        self.slider.valueChanged.connect(self._update_label)
        if on_value_changed is not None:
            self.slider.valueChanged.connect(on_value_changed)

        layout.setContentsMargins(0, 0, 0, 0)
        if name is not None:
            if label_editable:
                self._name_widget = LabelEditable(name)
                self._name_widget.editingCommitted.connect(self.editingCommitted)
            else:
                self._name_widget = QLabel(name)

            layout.addWidget(self._name_widget)

        layout.addWidget(self.slider)
        layout.addWidget(self.label)

        self._update_label_width()
        self._update_label(value)

    def name(self) -> str:
        if self._name_widget is None:
            return ""

        return self._name_widget.text()

    def _update_label(self, value):
        self.label.setText(f"{value}")

    def _update_label_width(self):
        current_text = self.label.text()

        widest_value_text = max(
            (str(self._label_minimum), str(self._label_maximum)),
            key=len,
        )

        self.label.setText(widest_value_text)
        self.label.ensurePolished()

        width = self.label.sizeHint().width()

        self.label.setFixedWidth(width)
        self.setMinimumWidth(max(self.minimumWidth(), width))

        self.label.setText(current_text)

    def hasFocus(self):
        return self.slider.hasFocus()

    def __getattr__(self, item):
        return getattr(self.slider, item)
