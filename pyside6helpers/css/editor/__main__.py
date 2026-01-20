import sys
from PySide6.QtWidgets import QApplication
from pyside6helpers.css.editor.ui.main_window import EditorMainWindow


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Frangitron")
    app.setApplicationName("CSS Editor 2")
    
    project_name = "demo"
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
        
    window = EditorMainWindow(project_name)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
