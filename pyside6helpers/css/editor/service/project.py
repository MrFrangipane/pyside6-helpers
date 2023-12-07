

class Project:
    def __init__(self, name):
        self.name = name
        self.template: dict[str: str] = dict()
        self.variables = dict()
        self.themes = dict()
        self.save_to: str = ""

    def __repr__(self):
        return f"<{self.__class__.__name__}(name='{self.name}')>"
