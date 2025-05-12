from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from app.schemas.category import (
    CategorySchema,
    UpdateCategorySchema,
    CreateCategorySchema,
)
from app.schemas.word import WordSchema, UpdateWordSchema, CreateWordSchema


class CreateCategoryWordsSchema(BaseModel):
    category: CreateCategorySchema
    words: List[CreateWordSchema]


class UpdateCategoryWordsSchema(BaseModel):
    category: UpdateCategorySchema
    words: List[UpdateWordSchema]


class CategoryWordsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    category: CategorySchema
    words: Optional[List[WordSchema]]
