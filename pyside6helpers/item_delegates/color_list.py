from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtWidgets import QStyledItemDelegate, QComboBox


class ColorListDelegate(QStyledItemDelegate):
    def __init__(self, colors_hex: list[str], parent=None):
        QStyledItemDelegate.__init__(self, parent)
        self._colors_hex = colors_hex

    def paint(self, painter, option, index):
        painter.save()
        color = QColor(index.data(Qt.DisplayRole))
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)
        painter.drawRect(option.rect.adjusted(1, 1, -1, -1))
        painter.restore()

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        for color_hex in self._colors_hex:
            color = QColor(color_hex)
            pixmap = QPixmap(20, 20)
            pixmap.fill(color)
            editor.addItem(QIcon(pixmap), color_hex)
        return editor

    def setEditorData(self, editor: QComboBox, index):
        editor.setCurrentText(index.data(Qt.DisplayRole))

    def setModelData(self, editor: QComboBox, model, index):
        model.setData(index, editor.currentText())
