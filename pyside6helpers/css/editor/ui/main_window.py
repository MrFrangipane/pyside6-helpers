import os

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QLabel, QPushButton, QButtonGroup, QRadioButton, QApplication
)
from PySide6.QtCore import Qt
from pyside6helpers.main_window import MainWindow

from ..project.persistence import ProjectPersistence
from ..project.css_renderer import CSSRenderer
from ..variables.ui.variables_widget import VariablesWidget
from ..templates.ui.template_editor_widget import TemplateEditorWidget
from ..preview.ui.preview_widget import PreviewWidget


class EditorMainWindow(MainWindow):
    def __init__(self, project_name="default"):
        super().__init__()

        app = QApplication.instance()
        app.aboutToQuit.connect(self._on_save_project)

        self.setWindowTitle(app.applicationName() + f" - {project_name}")

        self.project_name = project_name
        self.persistence = ProjectPersistence(project_name)
        self.renderer = CSSRenderer()
        self.project = self.persistence.load()
        
        self._setup_ui()
        self._load_project_into_ui()
        self._update_preview()

    def _setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Toolbar-like header
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel("Mode:"))

        self.mode_group = QButtonGroup(self)
        self.desktop_radio = QRadioButton("Desktop")
        self.touch_radio = QRadioButton("Touch")

        self.mode_group.addButton(self.desktop_radio)
        self.mode_group.addButton(self.touch_radio)

        self.disabled_button = QPushButton("Disabled")
        self.disabled_button.setCheckable(True)
        self.disabled_button.clicked.connect(self._on_disabled_changed)

        self.apply_to_editor_button = QPushButton("Apply to Editor")
        self.apply_to_editor_button.clicked.connect(self._on_apply_to_editor)

        self.clear_editor_button = QPushButton("Clear Editor style")
        self.clear_editor_button.clicked.connect(self._on_clear_editor)

        # Set default state
        self.desktop_radio.setChecked(True)

        header_layout.addWidget(self.desktop_radio)
        header_layout.addWidget(self.touch_radio)
        header_layout.addWidget(self.disabled_button)
        header_layout.addWidget(self.apply_to_editor_button)
        header_layout.addWidget(self.clear_editor_button)

        self.mode_group.buttonClicked.connect(self._on_mode_changed)
        
        header_layout.addStretch()
        
        self.save_project_button = QPushButton("Save project")
        self.save_project_button.clicked.connect(self._on_save_project)
        header_layout.addWidget(self.save_project_button)

        self.save_stylesheet_button = QPushButton("Save stylesheet")
        self.save_stylesheet_button.clicked.connect(self._on_save_stylesheet)
        header_layout.addWidget(self.save_stylesheet_button)

        layout.addLayout(header_layout)
        
        # Main Splitter
        self.main_splitter = QSplitter(Qt.Horizontal)
        
        # Left side: Variables and Templates
        self.left_splitter = QSplitter(Qt.Horizontal)
        
        self.variables_widget = VariablesWidget()
        self.variables_widget.changed.connect(self._on_data_changed)
        
        self.templates_widget = TemplateEditorWidget()
        self.templates_widget.changed.connect(self._on_data_changed)
        
        self.left_splitter.addWidget(self.variables_widget)
        self.left_splitter.addWidget(self.templates_widget)
        
        self.main_splitter.addWidget(self.left_splitter)
        
        # Right side: Preview
        self.preview_widget = PreviewWidget()
        self.main_splitter.addWidget(self.preview_widget)
        
        self.main_splitter.setStretchFactor(0, 1)
        self.main_splitter.setStretchFactor(1, 1)
        
        layout.addWidget(self.main_splitter)

    def _load_project_into_ui(self):
        self.variables_widget.set_variables(self.project.variables)
        self.templates_widget.set_sections(self.project.templates)
        self.statusBar().showMessage("Project loaded", 2000)

    def _on_apply_to_editor(self):
        mode = self.mode_group.checkedButton().text().lower()
        css = self.renderer.render(self.project, mode)
        self.setStyleSheet(css)

    def _on_clear_editor(self):
        self.setStyleSheet("")

    def _on_data_changed(self):
        self.project.variables = self.variables_widget.get_variables()
        self.project.templates = self.templates_widget.get_sections()
        self._update_preview()

    def _on_disabled_changed(self):
        self.preview_widget.setDisabled(self.disabled_button.isChecked())

    def _on_mode_changed(self, mode):
        self._update_preview()

    def _update_preview(self):
        mode = self.mode_group.checkedButton().text().lower()
        css = self.renderer.render(self.project, mode)
        self.preview_widget.setStyleSheet(css)

    def _on_save_project(self):
        self._on_data_changed()
        self.persistence.save_project(self.project)
        self.statusBar().showMessage("Project saved", 2000)

    def _on_save_stylesheet(self):
        self._on_data_changed()

        def save(mode):
            css = self.renderer.render(self.project, mode)
            filepath, extension = os.path.splitext(self.project.save_to_filepath)
            print(self.project.save_to_filepath, filepath, extension)
            with open(f"{filepath}-{mode}{extension}", "w") as f:
                f.write(css)

        save("desktop")
        save("touch")

        self.statusBar().showMessage("Stylesheet saved", 2000)
