import os.path

from pyside6helpers.python_extensions.singleton_metaclass import SingletonMetaclass


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
