from PySide6.QtWidgets import QFileDialog


def make_save_hook(title, name_filter, working_directory, callback):
    """Returns a callable that will getSaveFileName() and calls callback() if a file has been chosen"""
    def save_hook(self):
        dialog = QFileDialog()
        filepath, extension = dialog.getSaveFileName(None, title, working_directory, name_filter)
        if filepath:
            callback(filepath)

    return save_hook


def make_open_hook(title, name_filter, working_directory, callback):
    """Returns a callable that will getOpenFileName() and calls callback() if a file has been chosen"""
    def save_hook(self):
        dialog = QFileDialog()
        filepath, extension = dialog.getOpenFileName(None, title, working_directory, name_filter)
        if filepath:
            callback(filepath)

    return save_hook
