from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide6.QtCore import Qt


class BooleanDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor: QLineEdit, index):
        editor.setText("X" if index.data(Qt.DisplayRole) else "")

    def setModelData(self, editor: QLineEdit, model, index):
        model.setData(index, bool(editor.text().strip()))

    def displayText(self, value, locale):
        return "X" if value else ""
