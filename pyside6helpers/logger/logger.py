import sys
from io import TextIOWrapper
from PySide6.QtCore import QObject, Signal


class Logger(QObject):
    written = Signal(str)

    def __init__(self, stream: TextIOWrapper, parent=None):
        super().__init__(parent)
        self.name = stream.name.strip('<>')
        self._stream = stream
        self._buffer = ""
        setattr(sys, self.name, self)

    def write(self, text):
        self._stream.write(text)
        self._buffer += text
        if text.endswith("\n"):
            self.written.emit(self._buffer.strip('\n'))
            self._buffer = ""

    def flush(self):
        self._stream.flush()

    def __del__(self):
        setattr(sys, self.name, getattr(sys, f"__{self.name}__"))
