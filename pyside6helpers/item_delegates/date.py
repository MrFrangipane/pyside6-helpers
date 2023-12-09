from datetime import date

import dateparser
from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit
from PySide6.QtCore import Qt

from pyside6helpers.python_extensions.date_serializer import DateSerializer


class DateDelegate(QStyledItemDelegate):
    def __init__(self, month=None, year=None, parent=None):
        QStyledItemDelegate.__init__(self, parent)
        self._month = month if month is not None else date.today().month
        self._year = year if year is not None else date.today().year

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        return editor

    def setEditorData(self, editor: QLineEdit, index):
        try:

            editor.setText(DateSerializer.serialize(index.data(Qt.DisplayRole)))
        except (TypeError, AttributeError):
            pass

    def setModelData(self, editor: QLineEdit, model, index):
        try:
            date_ = DateSerializer.deserialize(editor.text(), self._month, self._year)
            model.setData(index, date_)
        except ValueError:
            pass

    def displayText(self, value: date, locale):
        return DateSerializer.serialize(value)
