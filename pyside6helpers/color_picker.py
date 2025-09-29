from PySide6.QtWidgets import QWidget, QVBoxLayout, QSlider, QFrame
from PySide6.QtCore import Qt, Signal, QPointF, QSize
from PySide6.QtGui import QPainter, QColor, QPixmap
import math


class ColorPreview(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(40)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)
        self._color = QColor(255, 255, 255)

    def setColor(self, color):
        self._color = color
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.fillRect(self.rect().adjusted(1, 1, -1, -1), self._color)


class ColorWheel(QWidget):
    colorChanged = Signal(QColor)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 200)
        self.hue = 0
        self.saturation = 0
        self.value = 255
        self.pressed = False
        self._wheel_pixmap = None
        self._wheel_rect = None
        self._resize_timer = None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Invalidate the cached pixmap when resizing
        self._wheel_pixmap = None
        self._wheel_rect = self.rect()

    def drawWheel(self):
        """Create the cached color wheel pixmap"""
        if (self._wheel_pixmap is not None and
                self._wheel_rect == self.rect() and
                self._cached_value == self.value):
            return

        self._wheel_rect = self.rect()
        self._cached_value = self.value
        self._wheel_pixmap = QPixmap(self.size())
        self._wheel_pixmap.fill(Qt.transparent)

        painter = QPainter(self._wheel_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Calculate center and radius
        center = QPointF(self.width() / 2, self.height() / 2)
        radius = min(self.width(), self.height()) / 2 - 5

        # Draw color wheel
        for i in range(360):
            painter.setPen(QColor.fromHsv(i, 255, self.value))
            painter.save()
            painter.translate(center)
            painter.rotate(i)
            painter.drawLine(0, 0, radius, 0)
            painter.restore()

        # Draw saturation gradient
        for r in range(int(radius)):
            for angle in range(360):
                x = center.x() + r * math.cos(math.radians(angle))
                y = center.y() + r * math.sin(math.radians(angle))
                sat = (r / radius) * 255
                color = QColor.fromHsv(angle, int(sat), self.value)
                painter.setPen(color)
                painter.drawPoint(int(x), int(y))

        painter.end()

    def paintEvent(self, event):
        self.drawWheel()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw the cached wheel
        painter.drawPixmap(0, 0, self._wheel_pixmap)

        # Draw selector
        if self.pressed:
            center = QPointF(self.width() / 2, self.height() / 2)
            radius = min(self.width(), self.height()) / 2 - 5
            angle = self.hue
            dist = (self.saturation / 255.0) * radius
            x = center.x() + dist * math.cos(math.radians(angle))
            y = center.y() + dist * math.sin(math.radians(angle))
            painter.setPen(Qt.white if self.value < 128 else Qt.black)
            painter.drawEllipse(QPointF(x, y), 4, 4)

    def mousePressEvent(self, event):
        self.pressed = True
        self.updateColor(event.position())
        self.update()

    def mouseMoveEvent(self, event):
        self.updateColor(event.position())
        self.update()

    def mouseReleaseEvent(self, event):
        self.pressed = False
        self.update()

    def updateColor(self, pos):
        center = QPointF(self.width() / 2, self.height() / 2)
        dx = pos.x() - center.x()
        dy = pos.y() - center.y()

        # Calculate hue
        angle = math.degrees(math.atan2(dy, dx))
        if angle < 0:
            angle += 360
        self.hue = angle

        # Calculate saturation
        distance = math.sqrt(dx * dx + dy * dy)
        radius = min(self.width(), self.height()) / 2 - 5
        self.saturation = min(255, int((distance / radius) * 255))

        self.colorChanged.emit(QColor.fromHsv(int(self.hue), self.saturation, self.value))


class ColorPicker(QWidget):
    colorChanged = Signal(QColor)

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        # Create color wheel
        self.wheel = ColorWheel(self)
        layout.addWidget(self.wheel)

        # Create value (luminance) slider
        self.value_slider = QSlider(Qt.Horizontal)
        self.value_slider.setRange(0, 255)
        self.value_slider.setValue(255)
        layout.addWidget(self.value_slider)

        # Create color preview
        self.preview = ColorPreview(self)
        layout.addWidget(self.preview)

        # Connect signals
        self.wheel.colorChanged.connect(self._onColorChanged)
        self.value_slider.valueChanged.connect(self.onValueChanged)

    def _onColorChanged(self, color):
        self.preview.setColor(color)
        self.colorChanged.emit(color)

    def onValueChanged(self, value):
        self.wheel.value = value
        self.wheel._wheel_pixmap = None  # Invalidate cache when value changes
        self.wheel.update()
        color = QColor.fromHsv(int(self.wheel.hue), self.wheel.saturation, value)
        self._onColorChanged(color)

    def color(self):
        return QColor.fromHsv(int(self.wheel.hue), self.wheel.saturation, self.wheel.value)

    def setColor(self, color):
        h, s, v = color.hue(), color.saturation(), color.value()
        self.wheel.hue = h
        self.wheel.saturation = s
        self.wheel.value = v
        self.value_slider.setValue(v)
        self.preview.setColor(color)
        self.wheel.update()


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    picker = ColorPicker()
    picker.show()
    app.exec()
