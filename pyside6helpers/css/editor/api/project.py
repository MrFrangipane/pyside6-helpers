from ..service.project import Project
from ..service.project_persitence import ProjectPersistence


def load(project_name) -> Project:
    loader = ProjectPersistence(project_name)
    return loader.load()


def save(project: Project) -> None:
    saver = ProjectPersistence(project.name)
    saver.save(project)
