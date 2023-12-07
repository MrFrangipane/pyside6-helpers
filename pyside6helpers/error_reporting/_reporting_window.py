import sys

from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QDialog, QPlainTextEdit, QLabel, QGridLayout,QApplication, QStyle, QPushButton, QGroupBox

from ._traceback_highlighter import _TracebackHighlighter


ICON_SIZE = 24  # http://srinikom.github.io/pyside-docs/PySide/QtGui/QStyle.html#PySide.QtGui.PySide.QtGui.QStyle.StandardPixmap


class _ReportingWindow(QDialog):
    def __init__(self, name, message, traceback, exit_on_error, parent=None):
        QDialog.__init__(self, parent)
        icon = self.style().standardIcon(QStyle.SP_MessageBoxCritical)

        self._exit_on_error = exit_on_error

        self.setWindowTitle(f"{name} error !")
        self.setWindowIcon(icon)

        try:
            font = QFontDatabase().systemFont(QFontDatabase.FixedFont)
        except AttributeError as e:
            font = QFont()
            font.setStyleHint(QFont.TypeWriter)

        #
        # Main widgets
        label_icon = QLabel()
        label_icon.setPixmap(icon.pixmap(ICON_SIZE, ICON_SIZE))

        label_message = QLabel(message)
        if len(message) > 200:
            label_message.setWordWrap(True)

        if self._exit_on_error:
            button_close = QPushButton('Exit')
            button_close.clicked.connect(sys.exit)
        else:
            button_close = QPushButton('Close')
            button_close.clicked.connect(self.accept)

        #
        # Traceback GroupBox
        self.text_traceback = QPlainTextEdit()
        self.text_traceback.setFont(font)
        self.text_traceback.setReadOnly(True)
        self.text_traceback.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.text_traceback.setPlainText(traceback)
        self.text_traceback.setVisible(False)
        self.text_traceback.setMinimumWidth(400)
        _TracebackHighlighter(self.text_traceback.document())

        self.button_copy = QPushButton('Copy to clipboard')
        self.button_copy.setProperty("secondary", True)
        self.button_copy.setVisible(False)
        self.button_copy.clicked.connect(self._copy)

        self.traceback_group = QGroupBox("Show details")
        self.traceback_group.setCheckable(True)
        self.traceback_group.setChecked(False)
        self.traceback_group.toggled.connect(self._toggle_details)

        traceback_layout = QGridLayout(self.traceback_group)
        traceback_layout.addWidget(self.text_traceback)
        traceback_layout.addWidget(self.button_copy)

        #
        # Main Layout
        layout = QGridLayout(self)
        layout.addWidget(label_icon, 0, 0)
        layout.addWidget(label_message, 0, 1)
        layout.addWidget(self.traceback_group, 1, 0, 1, 2)
        layout.addWidget(button_close, 2, 0, 1, 2)
        layout.setColumnStretch(1, 100)
        layout.setSizeConstraint(QGridLayout.SetFixedSize)

        self.setModal(True)

    def _toggle_details(self):
        self.text_traceback.setVisible(self.traceback_group.isChecked())
        self.button_copy.setVisible(self.traceback_group.isChecked())

    def _copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('```\n' + self.text_traceback.toPlainText() + '\n```')

    def reject(self):
        if self._exit_on_error:
            sys.exit()

        QDialog.reject(self)
