import os.path

import jinja2
from PySide6.QtCore import Qt, QObject, QTimer
from PySide6.QtWidgets import QApplication

from pyside6helpers.error_reporting import error_reported
from pyside6helpers.main_window import MainWindow

from .. import api
from ..service.project import Project
from ..service.project_persitence import ProjectPersistence

from .central_widget import CentralWidget


COLOR_VARIANTS = [
    10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95
]


def _make_main_window(project: Project, central_widget) -> MainWindow:
    main_window = MainWindow(
        settings_tuple=("Frangitron", "CSS Editor 2")
    )
    main_window.setCentralWidget(central_widget)
    main_window.setWindowTitle(f"CSS Editor 2 ({project.name})")

    return main_window


class Application(QObject):
    def __init__(self, project_name, styled_widget=None, parent=None):
        QObject.__init__(self, parent)

        if styled_widget is not None:
            self._styled_widget = styled_widget
        else:
            self._styled_widget = QApplication.topLevelWidgets()[0]

        self._rendering_needed = True

        self._project = api.project.load(project_name)

        self._central_widget = CentralWidget(self._project)
        self._central_widget.templateChanged.connect(self._template_changed)
        self._central_widget.variablesChanged.connect(self._variable_changed)
        self._central_widget.saveToChanged.connect(self._save_to_changed)
        self._central_widget.exportAllThemesRequested.connect(self._export_all)
        self._central_widget.template = self._project.template
        self._central_widget.variables = self._project.variables

        self._render_timer = QTimer()
        self._render_timer.timeout.connect(self._render)
        self._render_timer.setInterval(500)

        self._main_window = _make_main_window(self._project, self._central_widget)
        self._main_window.show()
        self._render_timer.start()

    @error_reported('Stylesheet rendering')
    def _render(self):
        # FIXME : move this to api
        if not self._rendering_needed:
            return

        template_fulltext = "\n".join(self._project.template.values())

        try:
            template_jj = jinja2.Template(template_fulltext)
            stylesheet = template_jj.render(**self._render_variables(self._project.variables))
            self._styled_widget.setStyleSheet(stylesheet)
            api.project.save(self._project)

        except jinja2.TemplateError:
            pass

        self._rendering_needed = False

    @staticmethod
    def _render_variables(variables):
        # FIXME : move this to api
        rendered_variables = dict()

        for name, value in variables.items():
            if isinstance(value, list) and len(value) == 3:
                rendered_variables[name] = 'rgb({})'.format(', '.join([str(channel) for channel in value]))

                for variant in COLOR_VARIANTS:
                    channels = [str(int(channel * variant * 0.01)) for channel in value]
                    rendered_variables['{}{:02d}'.format(name, variant)] = 'rgb({})'.format(', '.join(channels))

            else:
                rendered_variables[name] = value

        return rendered_variables

    @error_reported('Template change')
    def _template_changed(self):  # FIXME : called for every tab when loading project /!\
        self._project.template = self._central_widget.template
        self._rendering_needed = True

    @error_reported('Variable change')
    def _variable_changed(self):
        self._project.variables = self._central_widget.variables
        self._rendering_needed = True

    @error_reported('Export all themes')
    def _export_all(self):
        # FIXME : move this to api
        template_fulltext = "\n".join(self._project.template.values())

        template_jj = jinja2.Template(template_fulltext)
        stylesheet = template_jj.render(**self._render_variables(self._project.variables))

        stylesheet_filepath = os.path.join(self._project.save_to)

        with open(stylesheet_filepath, 'w') as stylesheet_file:
            stylesheet_file.write(stylesheet)

    @error_reported('Save to changed')
    def _save_to_changed(self):
        self._project.save_to = self._central_widget.save_to
