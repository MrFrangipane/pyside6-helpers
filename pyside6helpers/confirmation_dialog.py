from PySide6.QtWidgets import QApplication, QMessageBox


def confirmation_dialog(message: str) -> bool:
    """Show a confirmation warning QMessageBox with Ok / Cancel buttons"""
    confirmation_box = QMessageBox(QApplication.activeWindow())
    confirmation_box.setIcon(QMessageBox.Icon.Warning)
    confirmation_box.setWindowTitle("Are you sure ?")
    confirmation_box.setText(message)
    confirmation_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    result = confirmation_box.exec() == QMessageBox.Ok
    confirmation_box.deleteLater()

    return result
