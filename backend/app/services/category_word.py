from dataclasses import dataclass
from typing import Optional, List

from backend.app.exceptions import ConstraintViolationException, NotFoundException
from backend.app.repository import CategoryWordRepository
from backend.app.schemas import (
    CategoryWordsSchema,
    CategorySchema,
    WordSchema,
)


@dataclass
class CategoryWordService:

    repository: CategoryWordRepository

    # async def create(self, new_data: CreateCategorySchema) -> CategorySchema:
    #     if await self.repository.get_by_title(new_data.title):
    #         raise ConstraintViolationException()
    #     data = await self.repository.create(new_data)
    #
    #     return CategorySchema.model_validate(data)

    async def get_category_with_words(self, id: int) -> CategoryWordsSchema:
        category_db, words_db = await self.repository.get_category_with_words(id)
        if not category_db:
            raise NotFoundException()

        category = CategorySchema.model_validate(category_db)
        words = [WordSchema.model_validate(word) for word in words_db]

        return CategoryWordsSchema(category=category, words=words)

    # async def update(self, update_data: UpdateCategorySchema) -> CategorySchema:
    #     data = await self.repository.update(update_data)
    #
    #     return CategorySchema.model_validate(data)
    #
    # async def delite(self, id: int):
    #     return await self.repository.delete(id)
