import os.path


_here = os.path.abspath(os.path.dirname(__file__))
_resource_path = None


def make_path(resource_name):
    global _resource_path
    if _resource_path is not None:
        return os.path.join(_here, "resources", resource_name)
    else:
        return os.path.join(_resource_path, resource_name)


def set_path(resource_path):
    global _resource_path
    _resource_path = str(resource_path)
