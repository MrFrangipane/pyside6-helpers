from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import Qt


class ListDelegate(QStyledItemDelegate):
    def __init__(self, items: list[str], parent=None):
        QStyledItemDelegate.__init__(self, parent)
        self._items = items

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.addItems(self._items)
        return editor

    def setEditorData(self, editor: QComboBox, index):
        editor.setCurrentText(index.data(Qt.DisplayRole))

    def setModelData(self, editor: QComboBox, model, index):
        model.setData(index, editor.currentText())
