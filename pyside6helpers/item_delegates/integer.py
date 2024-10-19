from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide6.QtCore import Qt


class IntegerDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor: QLineEdit, index):
        editor.setText(str(index.data(Qt.DisplayRole)))

    def setModelData(self, editor: QLineEdit, model, index):
        model.setData(index, int(editor.text().strip()))

    def displayText(self, value, locale):
        return str(value)
