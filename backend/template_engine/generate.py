from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept as DB_Model
from mako.template import Template

from backend.template_engine.name_converter import converter
from backend.template_engine.settings import GeneratorSettings, settings
from app.database import Category
from backend.template_engine.mako_model import MakoModel


class Generator:
    changes: list = [
        ("schema", "schemas"),
        ("repository", "repository"),
        ("service", "services"),
        ("handler", "handlers"),
    ]

    def __init__(self, model: DB_Model):
        self.settings: GeneratorSettings = settings
        self.model: MakoModel = MakoModel(model=model)
        for item in self.changes:
            self.make_template(*item)

    def make_template(self, template: str, directory: str):
        template = Template(filename=f"{self.settings.mako_root}{template}.py.mako")
        filename = self._make_filename(directory)
        data = template.render(name=self.model.model_name, fields=self.model.fields)
        self._write_file(filename=filename, data=data)

    def _make_filename(self, directory):
        # return f"{converter(self.model.model_name)}.py"
        return (
            f"{self.settings.app_root}/"
            f"{directory}/"
            f"{converter(self.model.model_name)}_test.py"
        )

    @staticmethod
    def _write_file(filename: str, data: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)


if __name__ == "__main__":
    generator = Generator(Category)
