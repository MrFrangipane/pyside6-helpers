from PySide6.QtWidgets import QApplication, QMessageBox


def critical_box(message: str) -> None:
    """Show a critical QMessageBox with Ok buttons"""
    _exec_box(
        icon=QMessageBox.Icon.Critical,
        title="Critical",
        message=message
    )


def information_box(message: str) -> None:
    """Show an information QMessageBox with Ok buttons"""
    _exec_box(
        icon=QMessageBox.Icon.Information,
        title="Information",
        message=message
    )


def confirmation_box(message: str) -> bool:
    """Show a confirmation QMessageBox with Ok & Cancel buttons"""
    return _exec_box(
        icon=QMessageBox.Icon.Question,
        title="Are you sure ?",
        message=message,
        has_cancel=True
    )


def _exec_box(icon, title, message, has_cancel=False) -> bool:
    _box = QMessageBox(QApplication.activeWindow())
    _box.setIcon(icon)
    _box.setWindowTitle(title)
    _box.setText(message)
    if has_cancel:
        _box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    else:
        _box.setStandardButtons(QMessageBox.Ok)

    result = _box.exec() == QMessageBox.Ok
    _box.deleteLater()

    return result
