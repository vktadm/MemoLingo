from sqlalchemy import inspect
from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept as DB_Model
from dataclasses import dataclass

from backend.template_engine.python_mapper import mapper


@dataclass
class MakoField:
    name: str
    f_type: str
    unique: bool
    nullable: bool


class MakoModel:
    def __init__(self, model: DB_Model):
        self.model = model
        self.model_name = model.__name__
        self._init_fields()

    def _init_fields(self):
        inspector = inspect(self.model)
        self.fields = []

        for column in inspector.columns:
            current = {
                "name": column.name,
                "f_type": mapper(column.type),
                "unique": column.unique,
                "nullable": column.nullable,
            }
            self.fields.append(MakoField(**current))
