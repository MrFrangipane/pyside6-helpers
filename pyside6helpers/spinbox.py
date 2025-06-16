from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSpinBox, QDoubleSpinBox


class _BaseSpinBox(QWidget):  # FIXME autocompletion ?

    _spinBoxClass = None

    def __init__(self, name="", minimum=0, maximum=0, value=0, single_step=1, on_value_changed=None, parent=None):
        QWidget.__init__(self, parent)

        self.spinbox = self._spinBoxClass()
        layout = QHBoxLayout(self)

        self.spinbox.setSingleStep(single_step)
        self.spinbox.setMinimum(minimum)
        self.spinbox.setMaximum(maximum)
        self.spinbox.setValue(value)

        self.label = QLabel(name)

        if on_value_changed is not None:
            self.spinbox.valueChanged.connect(on_value_changed)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)
        layout.addWidget(self.spinbox)
        layout.setStretch(0, 100)

    def __getattr__(self, item):
        return getattr(self.spinbox, item)



class SpinBox(_BaseSpinBox):
    """
    Thin wrapper for a QSpinBox that shows its name
    """
    _spinBoxClass = QSpinBox


class DoubleSpinBox(_BaseSpinBox):
    """
    Thin wrapper for a QDoubleSpinBox that shows its name
    """
    _spinBoxClass = QDoubleSpinBox
