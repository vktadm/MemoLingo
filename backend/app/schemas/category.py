from typing import Optional
from pydantic import BaseModel, ConfigDict


class BaseCategorySchema(BaseModel):
    title: str
    translation: Optional[str]
    description: Optional[str]
    icon: Optional[str]


class CreateCategorySchema(BaseCategorySchema):
    title: str
    translation: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None


class UpdateCategorySchema(CreateCategorySchema):
    title: Optional[str] = None
    id: Optional[int] = None


class CategorySchema(BaseCategorySchema):
    model_config = ConfigDict(from_attributes=True)
    id: int
