import os.path

from pyside6helpers.python_extensions.singleton_metaclass import SingletonMetaclass


_here = os.path.abspath(os.path.dirname(__file__))


class _Resources(metaclass=SingletonMetaclass):
    root = None


def make_path(resource_name):
    if _Resources().root is None:
        return os.path.join(_here, "resources", resource_name)
    else:
        return os.path.join(_Resources().root, resource_name)


def set_path(resource_path):
    _Resources().root = resource_path
