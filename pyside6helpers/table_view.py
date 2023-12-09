from PySide6.QtWidgets import QTableView


def resize_columns_to_content_with_padding(table_view: QTableView, padding: int):
    table_view.resizeColumnsToContents()
    for section in range(table_view.horizontalHeader().count()):
        table_view.setColumnWidth(section, table_view.columnWidth(section) + padding)
