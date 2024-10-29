import sys

from PySide6.QtWidgets import QApplication

from pyside6helpers.css.editor import CSSEditor
from pyside6helpers.css.editor.ui.widgets_to_style import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # css.load_onto(window)
    editor = CSSEditor("Frangitron", styled_widget=window)

    sys.exit(app.exec())
