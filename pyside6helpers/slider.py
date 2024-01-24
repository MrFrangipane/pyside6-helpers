from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider


class Slider(QWidget):  # FIXME autocompletion ?
    """
    Thin wrapper for a QSlider that shows its value
    """
    def __init__(self, is_vertical=False, minimum=0, maximum=0, value=0, single_step=1, on_value_changed=None, parent=None):
        QWidget.__init__(self, parent)

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

        self.slider.valueChanged.connect(self._update_label)
        if on_value_changed is not None:
            self.slider.valueChanged.connect(on_value_changed)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.slider)
        layout.addWidget(self.label)

        self._update_label(value)

    def _update_label(self, value):
        self.label.setText(f"{value}")

    def __getattr__(self, item):
        return getattr(self.slider, item)
