import os.path
import sys

from pythonhelpers.singleton_metaclass import SingletonMetaclass


class _Resources(metaclass=SingletonMetaclass):
    default_root: str = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources")
    root: str = ""


def make_path(resource_name: str = "") -> str:
    root = _Resources().default_root if not _Resources().root else _Resources().root
    if not resource_name:
        return root

    return os.path.join(root, resource_name)


def set_root(root_path: str) -> None:
    _Resources().root = root_path


def find(resource_name: str, current_file: str | None = None) -> str:
    if current_file is None:
        current_file = sys.argv[0]

    current_dir = os.path.abspath(os.path.dirname(current_file))
    resources_dir = "resources"

    while current_dir:
        potential_resources_path = os.path.join(current_dir, resources_dir)
        if os.path.isdir(potential_resources_path):
            path = os.path.join(potential_resources_path, resource_name)
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Could not find {resource_name} in {potential_resources_path}")
            return path

        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            break

        current_dir = parent_dir

    raise FileNotFoundError(f"Could not find a 'resources' folder starting from {current_file}")
