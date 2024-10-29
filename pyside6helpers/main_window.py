from PySide6.QtCore import QSettings, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    shown = Signal()

    def __init__(self, logo_filepath: str = "", settings_tuple: tuple[str, str] = tuple()):
        super().__init__()

        if logo_filepath:
            logo_pixmap = QPixmap(logo_filepath)
            logo_label = QLabel()
            logo_label.setPixmap(logo_pixmap)
            self.statusBar().addPermanentWidget(logo_label)

        self._settings_tuple = settings_tuple

        self.load_geometry()

    def closeEvent(self, event):
        self.save_geometry()
        super().closeEvent(event)
        event.accept()

    def showEvent(self, event):
        self.shown.emit()
        event.accept()

    def save_geometry(self):
        if self._settings_tuple:
            settings = QSettings(*self._settings_tuple)
            settings.setValue('geometry', self.saveGeometry())
            settings.setValue('state', self.saveState())

    def load_geometry(self):
        if self._settings_tuple:
            settings = QSettings(*self._settings_tuple)
            self.restoreGeometry(settings.value('geometry'))
            self.restoreState(settings.value('state'))
