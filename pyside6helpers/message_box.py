from PySide6.QtWidgets import QApplication, QMessageBox


def critical_box(message_lines: list[str]) -> None:
    """Show a critical QMessageBox with Ok button"""
    _exec_box(
        icon=QMessageBox.Icon.Critical,
        title="Critical",
        message_lines=message_lines
    )


def warning_box(message_lines: list[str]) -> None:
    """Show a warning QMessageBox with Ok button"""
    _exec_box(
        icon=QMessageBox.Icon.Warning,
        title="Information",
        message_lines=message_lines
    )


def information_box(message_lines: list[str]) -> None:
    """Show an information QMessageBox with Ok button"""
    _exec_box(
        icon=QMessageBox.Icon.Information,
        title="Information",
        message_lines=message_lines
    )


def confirmation_box(message_lines: list[str]) -> bool:
    """Show a confirmation QMessageBox with Ok & Cancel buttons"""
    return _exec_box(
        icon=QMessageBox.Icon.Question,
        title="Are you sure ?",
        message_lines=message_lines,
        has_cancel=True
    )


def _exec_box(icon: QMessageBox.Icon, title: str, message_lines: list[str], has_cancel=False) -> bool:
    _box = QMessageBox(QApplication.activeWindow())
    _box.setIcon(icon)
    _box.setWindowTitle(title)
    _box.setText("\n".join(message_lines))
    if has_cancel:
        _box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    else:
        _box.setStandardButtons(QMessageBox.Ok)

    result = _box.exec() == QMessageBox.Ok
    _box.deleteLater()

    return result
