import os
import json
from typing import List, Any
from jinja2 import Environment, FileSystemLoader


class TableDiagram:
    def __init__(self) -> None:
        self.template_name = "table.html"
        self.template_directory = os.path.dirname(__file__)
        self.scope = {}

    def add_scope(self, key: str, value: Any):
        self.scope[key] = value

    def generate_html_file(
        self,
        json_tables: List[Any],
        json_relationships: List[Any],
        output_file: str,
    ):
        self.add_scope("diagram_tables", json.dumps(json_tables))
        self.add_scope("diagram_relationships", json.dumps(json_relationships))

        env_loader = Environment(
            loader=FileSystemLoader(searchpath=os.path.realpath(self.template_directory))
        )

        html_template = env_loader.get_template(self.template_name).render(self.scope)
        file = open(os.path.join(self.template_directory, output_file), "w", encoding="utf-8")
        file.write(html_template)
        file.close()
