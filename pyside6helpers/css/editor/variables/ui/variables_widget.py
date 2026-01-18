from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import (
    QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, 
    QPushButton, QHBoxLayout, QHeaderView
)
from .variable_sliders import VariableSliders
from ...project.models import Variable


class VariablesWidget(QWidget):
    changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        self.layout = QVBoxLayout(self)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Desktop", "Touch", ""])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.table.setColumnWidth(3, 30)

        self.table.itemChanged.connect(self._on_item_changed)
        self.table.currentItemChanged.connect(self._on_current_item_changed)

        self.sliders = VariableSliders()
        self.sliders.setEnabled(False)
        self.sliders.changed.connect(self._on_slider_changed)

        self.add_button = QPushButton("Add Variable")
        self.add_button.clicked.connect(self._on_add_variable)

        self.layout.addWidget(self.table)
        self.layout.addWidget(self.sliders)
        self.layout.addWidget(self.add_button)

    def set_variables(self, variables: list[Variable]):
        self.table.blockSignals(True)
        self.table.setRowCount(0)
        for var in variables:
            self._add_row(var)
        self.table.blockSignals(False)

    def get_variables(self) -> list[Variable]:
        variables = []
        for row in range(self.table.rowCount()):
            name_item = self.table.item(row, 0)
            desktop_item = self.table.item(row, 1)
            touch_item = self.table.item(row, 2)
            if name_item and desktop_item and touch_item:
                variables.append(Variable(
                    name=name_item.text(),
                    desktop_value=desktop_item.text(),
                    touch_value=touch_item.text()
                ))
        return variables

    def _add_row(self, var: Variable):
        row = self.table.rowCount()
        self.table.insertRow(row)

        name_item = QTableWidgetItem(var.name)
        desktop_item = QTableWidgetItem(var.desktop_value)
        touch_item = QTableWidgetItem(var.touch_value)

        delete_button = QPushButton("X")
        delete_button.clicked.connect(self._on_delete_variable)

        self.table.setItem(row, 0, name_item)
        self.table.setItem(row, 1, desktop_item)
        self.table.setItem(row, 2, touch_item)
        self.table.setCellWidget(row, 3, delete_button)

    def _on_add_variable(self):
        var = Variable("new_variable", "[255, 255, 255]", "[255, 255, 255]")
        self.table.blockSignals(True)
        self._add_row(var)
        self.table.blockSignals(False)
        self.changed.emit()

    def _on_delete_variable(self):
        # We need to find the row again because it might have changed
        button = self.sender()
        for r in range(self.table.rowCount()):
            if self.table.cellWidget(r, 3) == button:
                self.table.removeRow(r)
                break
        self.changed.emit()

    def _on_item_changed(self, item):
        self.changed.emit()

    def _on_current_item_changed(self, current, previous):
        if current and current.column() in (1, 2):
            text = current.text().strip()
            if text.startswith('[') and text.endswith(']'):
                try:
                    r, g, b = [int(c.strip()) for c in text[1:-1].split(',')]
                    self.sliders.setEnabled(True)
                    self.sliders.set_rgb(r, g, b)
                    return
                except ValueError:
                    pass
        self.sliders.setEnabled(False)

    def _on_slider_changed(self, r, g, b):
        item = self.table.currentItem()
        if item and item.column() in (1, 2):
            self.table.blockSignals(True)
            item.setText(f"[{r}, {g}, {b}]")
            self.table.blockSignals(False)
            self.changed.emit()
