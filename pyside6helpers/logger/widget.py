import sys

from PySide6.QtGui import QTextOption, QTextCursor
from PySide6.QtWidgets import QWidget, QPlainTextEdit, QGridLayout, QPushButton, QApplication

from pyside6helpers import icons

from pyside6helpers.logger.logger import Logger
from pyside6helpers.logger.text_highlighter import TextHighlighter


class LoggerWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._logger_stdout = Logger(sys.stdout)
        self._logger_stdout.written.connect(self.append_to_log)
        self._logger_stderr = Logger(sys.stderr)
        self._logger_stderr.written.connect(self.append_to_log)

        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setWordWrapMode(QTextOption.NoWrap)
        self.text_highlighter = TextHighlighter(self.text_edit.document())

        self.button_scroll_to_end = QPushButton()
        self.button_scroll_to_end.setIcon(icons.down_arrow())
        self.button_scroll_to_end.setToolTip("Scroll to bottom")
        self.button_scroll_to_end.clicked.connect(self._scroll_to_end)

        self.button_clear = QPushButton()
        self.button_clear.setIcon(icons.trash())
        self.button_clear.setToolTip("Clear all")
        self.button_clear.clicked.connect(self.text_edit.clear)

        layout = QGridLayout(self)
        layout.addWidget(self.text_edit, 0, 0, 3, 1)
        layout.addWidget(self.button_scroll_to_end, 0, 1)
        layout.addWidget(self.button_clear, 1, 1)
        layout.addWidget(QWidget(), 2, 1)
        layout.setRowStretch(2, 100)

    def append_to_log(self, text):
        self.text_edit.appendPlainText(text)
        QApplication.processEvents()

    def _scroll_to_end(self):
        self.text_edit.moveCursor(QTextCursor.End)
        self.text_edit.ensureCursorVisible()
