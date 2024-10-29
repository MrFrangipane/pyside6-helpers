from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QTabWidget

from ..service.project import Project
from .tabbed_template_editor import TabbedTemplateEditor
from .variables import Variables


class CentralWidget(QWidget):
    templateChanged = Signal()
    variablesChanged = Signal()
    saveToChanged = Signal()
    exportAllThemesRequested = Signal()

    def __init__(self, project, parent=None):
        QWidget.__init__(self, parent)

        self._project: Project = project

        self._app = QApplication.instance()

        self._template_tabs = TabbedTemplateEditor()
        self._template_tabs.changed.connect(self.templateChanged)

        self._variables = Variables()
        self._variables.changed.connect(self.variablesChanged)

        self._new_theme_button = QPushButton("new theme")
        self._new_theme_button.setEnabled(False)
        self._delete_theme_button = QPushButton("delete theme")
        self._delete_theme_button.setEnabled(False)

        self._export_all_themes = QPushButton("Export all themes")
        self._export_all_themes.clicked.connect(self.exportAllThemesRequested)

        self._line_save_to = QLineEdit(self._project.save_to)
        self._line_save_to.textChanged.connect(self.saveToChanged)


        self._tabs = QTabWidget()
        self._tabs.addTab(self._template_tabs, "Template")
        self._tabs.addTab(self._variables, "Variables")

        layout = QGridLayout(self)
        layout.addWidget(self._tabs, 0, 0, 1, 2)
        # layout.addWidget(self._new_theme_button, 1, 1)
        # layout.addWidget(self._delete_theme_button, 1, 2)
        layout.addWidget(self._export_all_themes, 1, 0)
        layout.addWidget(self._line_save_to, 1, 1)

    @property
    def template(self):
        return self._template_tabs.sections

    @template.setter
    def template(self, sections):
        self._template_tabs.set_sections(sections)

    @property
    def variables(self):
        return self._variables.variables

    @variables.setter
    def variables(self, variables):
        self._variables.variables = variables

    @property
    def save_to(self):
        return self._line_save_to.text()

    @save_to.setter
    def save_to(self, value):
        self._line_save_to.setText(value)
