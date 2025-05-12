from typing import Optional
from pydantic import BaseModel, ConfigDict


class Base${name}Schema(BaseModel):
    % for item in fields:
    % if item.name != "id":
    ${item.name}: ${"Optional[" + item.f_type + "]" if item.nullable else item.f_type}
    % endif
    % endfor


class Create${name}Schema(Base${name}Schema):
    % for item in fields:
    % if item.name != "id":
    ${item.name}: ${"Optional[" + item.f_type + "]" + " = None" if item.nullable else item.f_type}
    % endif
    % endfor


class Update${name}Schema(Base${name}Schema):
    % for item in fields:
    ${item.name}: ${"Optional[" + item.f_type + "]" + " = None"}
    % endfor


class ${name}Schema(Base${name}Schema):
    model_config = ConfigDict(from_attributes=True)
    id: int
