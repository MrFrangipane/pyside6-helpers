from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QTableView


def resize_columns_to_content_with_padding(table_view: QTableView, padding: int):
    table_view.resizeColumnsToContents()
    for section in range(table_view.horizontalHeader().count()):
        table_view.setColumnWidth(section, table_view.columnWidth(section) + padding)


class TableView(QTableView):
    """
    QTableView with deletion key functionality
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self._internal_clipboard: dict[tuple[int, int], str] = dict()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Delete, Qt.Key_Backspace):
            selected_indexes = self.selectionModel().selectedIndexes()

            for index in selected_indexes:
                self.model().setData(index, "", Qt.EditRole)

        elif event.matches(QKeySequence.StandardKey.Copy):
            self._copy_to_clipboard()

        elif event.matches(QKeySequence.StandardKey.Paste):
            self._paste_from_clipboard()

        super().keyPressEvent(event)

    def _copy_to_clipboard(self):
        selected_indexes = self.selectionModel().selectedIndexes()
        if not selected_indexes:
            return

        self._internal_clipboard = dict()
        selected_indexes = sorted(
            selected_indexes, key=lambda index: (index.row(), index.column())
        )
        start_row = selected_indexes[0].row()
        start_col = selected_indexes[0].column()

        for index in selected_indexes:
            self._internal_clipboard[(index.row() - start_row, index.column() - start_col)] = index.data(Qt.DisplayRole) or ""

        print(self._internal_clipboard)

    def _paste_from_clipboard(self):
        if not self._internal_clipboard:
            return

        selected_indexes = self.selectionModel().selectedIndexes()
        if not selected_indexes:
            return

        selected_indexes = sorted(
            selected_indexes, key=lambda index: (index.row(), index.column())
        )
        start_row = selected_indexes[0].row()
        start_col = selected_indexes[0].column()

        for (row, column), value in self._internal_clipboard.items():
            if not value:
                continue

            self.model().setData(self.model().index(start_row + row, start_col + column), value, Qt.EditRole)
