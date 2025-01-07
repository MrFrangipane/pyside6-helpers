import io
import sys
from PySide6.QtCore import QObject, Signal


class StringIOCapture(QObject):
    # Define a signal that emits whenever the stream is written to
    written = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__()
        # Use composition to include StringIO functionality
        self.string_io = io.StringIO(*args, **kwargs)

    def write(self, s: str) -> int:
        """
        Write a string to the underlying StringIO buffer and emit the signal.
        """
        result = self.string_io.write(s)  # Delegate the write operation to the StringIO object
        self.written.emit(s.strip())  # Emit the signal with the written text
        sys.stderr.write(s)
        return result

    def writelines(self, lines) -> None:
        """
        Write multiple lines to the buffer and emit the signal for each line.
        """
        for line in lines:
            self.write(line)

    def getvalue(self) -> str:
        """Retrieve the entire contents of the buffer."""
        return self.string_io.getvalue()

    def close(self) -> None:
        """Close the underlying StringIO buffer."""
        self.string_io.close()

    def flush(self) -> None:
        """Flush the contents of the buffer."""
        self.string_io.flush()
