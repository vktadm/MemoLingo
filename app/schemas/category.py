from pydantic import BaseModel


class CategorySchema(BaseModel):
    title: str
    translation: str | None
    description: str | None
