from typing import List
from PySide6.QtWidgets import QComboBox


def update(combo: QComboBox, items: List[str], current_text="", reset: bool = False):
    if not reset:
        current_text = combo.currentText() if not current_text else current_text
    combo.blockSignals(True)
    combo.clear()

    if not items:
        return

    combo.addItems(items)
    try:
        combo.setCurrentIndex(items.index(current_text))
    except ValueError:
        combo.setCurrentIndex(-1)

    combo.blockSignals(False)


# def set_current_item(combo: QComboBox, item_text):
#     items = [combo.itemText(i) for i in range(combo.count())]
#     try:
#         combo.setCurrentIndex(items.index(item_text))
#         return True
#     except ValueError:
#         return False
