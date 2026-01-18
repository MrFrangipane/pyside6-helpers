import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QPropertyAnimation, Property, Signal, QEasingCurve
from PySide6.QtGui import QPainter, QPalette


class ConfirmButton(QPushButton):

    def __init__(self, text="", confirm_text="Sure ?", duration=1000, parent=None):
        super().__init__(text, parent)
        self._default_text = text
        self._confirm_text = confirm_text
        self._progress = 0.0

        # Setup the animation
        self.animation = QPropertyAnimation(self, b"progress")
        self.animation.setDuration(duration)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(100.0)
        # Use a linear curve for a steady progress bar
        self.animation.setEasingCurve(QEasingCurve.Type.Linear)

        # Connect animation finished signal
        self.animation.finished.connect(self._on_animation_finished)

    @Property(float)
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value
        self.update()  # Trigger a repaint to show the progress

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.setText(self._confirm_text)
            self.animation.start()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.animation.state() == QPropertyAnimation.State.Running:
                self.animation.stop()
                self._reset_button()
                return

        super().mouseReleaseEvent(event)

    def _on_animation_finished(self):
        # Only fire if we actually reached 100%
        if self._progress >= 100.0:
            self.clicked.emit()

        self._reset_button()

    def _reset_button(self):
        self._progress = 0.0
        self.setText(self._default_text)
        self.update()

    def paintEvent(self, event):
        # Draw the standard button first
        super().paintEvent(event)

        if self._progress > 0:
            painter = QPainter(self)
            # Create a semi-transparent overlay color
            color = self.palette().color(QPalette.ColorRole.Highlight)
            color.setAlpha(100)

            # Calculate the width of the progress bar based on current progress
            width = int(self.width() * (self._progress / 100.0))

            # Draw the progress rectangle
            painter.fillRect(0, 0, width, self.height(), color)
            painter.end()


# Example Usage
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    layout = QVBoxLayout(window)

    btn = ConfirmButton("Hold to Delete", "Sure ?", duration=1000)
    btn.setMinimumHeight(50)
    btn.setStyleSheet("font-size: 16px; padding: 10px; background-color: lightgray;")

    # Connect to our custom signal
    btn.clicked.connect(lambda: print("Clicked"))

    layout.addWidget(btn)
    window.show()
    sys.exit(app.exec())
