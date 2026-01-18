import sys
from PySide6.QtWidgets import QApplication
from pyside6helpers.css.editor.ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    
    project_name = "demo"
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
        
    window = MainWindow(project_name)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
