from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Variable:
    name: str
    desktop_value: str
    touch_value: str


@dataclass
class Project:
    name: str
    templates: Dict[str, str] = field(default_factory=dict)
    variables: List[Variable] = field(default_factory=list)
    save_to_filepath: str = ""
    
    def get_variables_dict(self, mode: str) -> Dict[str, str]:
        if mode == "desktop":
            return {v.name: v.desktop_value for v in self.variables}
        elif mode == "touch":
            return {v.name: v.touch_value if v.touch_value else v.desktop_value for v in self.variables}
        else:
            raise ValueError(f"Invalid mode: {mode}")
