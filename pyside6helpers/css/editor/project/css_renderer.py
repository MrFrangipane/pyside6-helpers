import re
from .models import Project


class CSSRenderer:
    def render(self, project: Project, mode: str) -> str:
        variables = project.get_variables_dict(mode)
        
        full_css = []
        for section_name, template in project.templates.items():
            rendered_section = template
            for var_name, var_value in variables.items():

                if var_value.startswith('[') and var_value.endswith(']'):
                    if len(var_value.split(',')) == 3:
                        var_value = f"rgb({var_value[1:-1]})"
                    elif len(var_value.split(',')) == 4:
                        var_value = f"rgba({var_value[1:-1]})"

                if var_value.startswith('{') and var_value.endswith('}'):
                    var_values = [var.strip() for var in var_value[1:-1].split(',')]
                    pattern = r'(\{\{\s*' + var_name + r'\s*\}\}):?\s?([^{\s]+)?'

                    def replace_func(match):
                        full_match = match.group(0)
                        selector = match.group(2)

                        if selector:
                            return ", ".join([f"{val}:{selector}" for val in var_values])
                        return ", ".join(var_values)

                    rendered_section = re.sub(pattern, replace_func, rendered_section)

                else:
                    pattern = r'\{\{\s*' + re.escape(var_name) + r'\s*\}\}'
                    rendered_section = re.sub(pattern, var_value, rendered_section)
            
            full_css.append(f"/* Section: {section_name} */")
            full_css.append(rendered_section)

        return "\n\n".join(full_css)
