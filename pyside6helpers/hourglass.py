from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt


class Hourglass:
    """
    Context manager to freeze and show a hourglass
    ````
    with Hourglass(self):
        # do lengthy stuff
    ````
    """

    def __init__(self, parent=None):
        if parent is None:
            parent = QApplication.topLevelWidgets()[0]  # TODO : are we sure of this ?
        self._parent = parent
        self._widget = QApplication.focusWidget()

    def __enter__(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self._parent.setEnabled(False)
        QApplication.processEvents()

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self._parent.setEnabled(True)
            self._widget.setFocus()
        except AttributeError:
            pass
        finally:
            QApplication.restoreOverrideCursor()
            QApplication.processEvents()
