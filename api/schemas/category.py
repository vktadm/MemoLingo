from pydantic import BaseModel, ConfigDict


class Category(BaseModel):
    title: str
    # description: str | None
