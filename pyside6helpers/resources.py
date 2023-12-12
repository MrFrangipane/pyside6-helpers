import os.path


_here = os.path.abspath(os.path.dirname(__file__))


def make_resource_path(resource_name):
    return os.path.join(_here, "resources", resource_name)
