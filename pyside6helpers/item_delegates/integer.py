from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide6.QtCore import Qt


class IntegerDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor: QLineEdit, index):
        value = index.data(Qt.DisplayRole)
        if value is not None:
            editor.setText(str(value))

    def setModelData(self, editor: QLineEdit, model, index):
        try:
            value = int(editor.text().strip())
        except ValueError:
            value = None

        model.setData(index, value)

    def displayText(self, value, locale):
        return str(value)
