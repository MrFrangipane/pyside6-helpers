from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLineEdit


class LabelEditable(QLineEdit):
    editingCommitted = Signal(str)

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)

        self.setReadOnly(True)
        self.setFrame(False)
        self.setCursor(Qt.ArrowCursor)
        self.setFocusPolicy(Qt.ClickFocus)

        self.editingFinished.connect(self._finish_editing)

        self.setStyleSheet("""
            QLineEdit {
                background: transparent;
                border: none;
                padding: 0px;
            }

            QLineEdit:focus {
                border: 1px solid palette(highlight);
                padding: 1px;
            }
        """)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.isReadOnly():
            self._start_editing()
            event.accept()
            return

        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.clearFocus()
            self.setReadOnly(True)
            self.setCursor(Qt.ArrowCursor)
            return

        super().keyPressEvent(event)

    def _start_editing(self):
        self.setReadOnly(False)
        self.setCursor(Qt.IBeamCursor)
        self.setFocus()
        self.selectAll()

    def _finish_editing(self):
        self.setReadOnly(True)
        self.setCursor(Qt.ArrowCursor)
        self.editingCommitted.emit(self.text())
