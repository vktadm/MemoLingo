from typing import Optional
from pydantic import BaseModel, ConfigDict


class BaseCategorySchema(BaseModel):
    title: str
    translation: Optional[str]
    description: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class CreateCategorySchema(BaseCategorySchema):
    description: Optional[str] = None


class UpdateCategorySchema(CreateCategorySchema):
    title: str = None
    translation: Optional[str] = None


class CategorySchema(BaseCategorySchema):
    id: int
    icon: Optional[str]
