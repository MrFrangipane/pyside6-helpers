import os
import json
from importlib import resources

from .models import Project, Variable


class ProjectPersistence:
    def __init__(self, project_name):
        self.project_name = project_name
        resource_path = resources.files("pyside6helpers.resources").joinpath(f"{project_name}.csseditor2.json")
        with resources.as_file(resource_path) as p:
            self._project_filename = p

    def load(self) -> Project:
        if not os.path.exists(self._project_filename):
            return Project(
                self.project_name,
                templates={"Main": "QPushButton {\n  background-color: rgb({{ primary_color }});\n  padding: {{ padding }};\n}"},
                variables=[
                    Variable("primary_color", "[0, 120, 215]", "[255, 100, 0]"),
                    Variable("padding", "5px", "20px")
                ]
            )

        with open(self._project_filename, "r") as f:
            data = json.load(f)

        variables = []
        for v_data in data.get('variables', []):
            if isinstance(v_data, dict):
                variables.append(Variable(
                    name=v_data['name'],
                    desktop_value=v_data['desktop_value'],
                    touch_value=v_data['touch_value']
                ))
            else:
                # Handle migration from the old format if necessary,
                # but here we focus on the new format
                pass

        return Project(
            name=self.project_name,
            templates={k: "\n".join(v) if isinstance(v, list) else v for k, v in data.get('templates', {}).items()},
            variables=variables,
            save_to_filepath=data.get('save_to_filepath', "")
        )

    def save_project(self, project: Project) -> None:
        data = {
            'version': 1,
            'templates': {k: v.splitlines() for k, v in project.templates.items()},
            'variables': [
                {
                    'name': v.name,
                    'desktop_value': v.desktop_value,
                    'touch_value': v.touch_value
                } for v in project.variables
            ],
            'save_to_filepath': project.save_to_filepath
        }
        with open(self._project_filename, "w") as f:
            json.dump(data, f, indent=2)
