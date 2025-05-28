from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from backend.src.app.schemas.category import (
    CategorySchema,
)
from backend.src.app.schemas.word import WordSchema, UpdateWordSchema, CreateWordSchema


class CreateCategoryWordSchema(BaseModel):
    category: CategorySchema
    word: CreateWordSchema


class UpdateCategoryWordSchema(BaseModel):
    category: CategorySchema
    word: UpdateWordSchema


class CategoryWordsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    category: CategorySchema
    words: Optional[List[WordSchema]]
