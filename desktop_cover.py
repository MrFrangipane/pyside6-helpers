import sys
import ctypes
from ctypes import wintypes

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QRect, Signal


def _get_taskbar_geometry():
    """Get Windows taskbar geometry (position and size)"""

    # Define necessary Windows API structures and functions
    class RECT(ctypes.Structure):
        _fields_ = [
            ("left", ctypes.c_long),
            ("top", ctypes.c_long),
            ("right", ctypes.c_long),
            ("bottom", ctypes.c_long)
        ]

    # Get handle to taskbar
    taskbar_handle = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)

    if taskbar_handle == 0:
        return None

    # Get taskbar rectangle
    rect = RECT()
    if ctypes.windll.user32.GetWindowRect(taskbar_handle, ctypes.byref(rect)):
        return {
            'x': rect.left,
            'y': rect.top,
            'width': rect.right - rect.left,
            'height': rect.bottom - rect.top,
            'right': rect.right,
            'bottom': rect.bottom
        }

    return None


def _get_work_area():
    """Get work area (screen minus taskbar)"""

    class RECT(ctypes.Structure):
        _fields_ = [
            ("left", ctypes.c_long),
            ("top", ctypes.c_long),
            ("right", ctypes.c_long),
            ("bottom", ctypes.c_long)
        ]

    rect = RECT()
    if ctypes.windll.user32.SystemParametersInfoW(48, 0, ctypes.byref(rect), 0):  # SPI_GETWORKAREA = 48
        return {
            'x': rect.left,
            'y': rect.top,
            'width': rect.right - rect.left,
            'height': rect.bottom - rect.top,
            'right': rect.right,
            'bottom': rect.bottom
        }

    return None


class DesktopCoverWindow(QMainWindow):
    """
    Borderless window with taskbar awareness.
    """

    closed = Signal()

    def __init__(self):
        super().__init__()

        # Set window flags for the desired behavior
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |  # Borderless
            Qt.WindowType.Tool |  # Doesn't show in taskbar
            Qt.WindowType.WindowStaysOnTopHint  # Keep on top initially
        )

        # Remove always on top behavior after setting initial flags
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)

        # Prevent minimizing on Windows+D
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)

        self.center_window()

    def center_window(self):
        work_area = _get_work_area()
        work_geometry = QRect(work_area['x'], work_area['y'], work_area['width'], work_area['height'])
        self.setGeometry(work_geometry)

    def closeEvent(self, event):
        self.closed.emit()
        event.accept()


def main():
    app = QApplication(sys.argv)

    window = DesktopCoverWindow()
    window.show()
    window.closed.connect(app.quit)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
