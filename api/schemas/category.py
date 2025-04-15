from pydantic import BaseModel, ConfigDict


class CategorySchema(BaseModel):
    title: str
    # description: str | None
