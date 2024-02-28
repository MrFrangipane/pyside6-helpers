import os
import json

from .project import Project
from pyside6helpers.resources import make_resource_path


class ProjectPersistence:
    def __init__(self, project_name):
        self.project_name = project_name
        self._project_filename = make_resource_path(f"{project_name}.csseditor.json")

    def load(self) -> Project:
        project = Project(self.project_name)

        if not os.path.exists(self._project_filename):
            return project

        with open(self._project_filename, "r") as project_file:
            project_raw = json.load(project_file)

        version = project_raw.get('version', 1)
        loaders = {
            1: self._load_1,
            2: self._load_2,
            3: self._load_3
        }
        return loaders[version](project_raw, project)

    def _load_1(self, project_raw, project):
        project.template = project_raw['template']
        project.variables = project_raw['variables']
        project.themes = project_raw['themes']

        return project

    def _load_2(self, project_raw, project):
        project.template = {section_name: "\n".join(lines) for section_name, lines in project_raw['template'].items()}
        project.variables = project_raw['variables']
        project.themes = project_raw['themes']

        return project

    def _load_3(self, project_raw, project):
        project.template = {section_name: "\n".join(lines) for section_name, lines in project_raw['template'].items()}
        project.variables = project_raw['variables']
        project.themes = project_raw['themes']
        project.save_to = project_raw['save_to']

        return project

    def save(self, project: Project) -> None:
        template_sections = {section_name: text.splitlines() for section_name, text in project.template.items() if text}

        project_raw = {
            'template': template_sections,
            'variables': project.variables,
            'themes': project.themes,
            'version': 3,
            'save_to': project.save_to
        }
        with open(self._project_filename, "w") as project_file:
            json.dump(project_raw, project_file, indent=2)
