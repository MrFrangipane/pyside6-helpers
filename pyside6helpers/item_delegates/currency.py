import locale

from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide6.QtCore import Qt


class CurrencyDelegate(QStyledItemDelegate):

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor: QLineEdit, index):
        editor.setText(str(index.data(Qt.DisplayRole)))

    def setModelData(self, editor: QLineEdit, model, index):
        try:
            model.setData(index, float(editor.text().strip()))
        except ValueError:
            pass

    def displayText(self, value, locale_):
        return locale.currency(value, grouping=True)
