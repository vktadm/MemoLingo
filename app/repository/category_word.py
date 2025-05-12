from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import joinedload

from app.database import Category, Word, CategoryWord
from app.decorators import handle_db_errors
from app.schemas import CreateCategoryWordsSchema, UpdateCategoryWordsSchema


@dataclass
class CategoryWordRepository:
    """
    Класс-репозиторий для работы с моделью в базе данных.
    Реализует CRUD (Create, Read, Update, Delete) операции.
    Использует асинхронный SQLAlchemy для работы с БД.
    """

    session: AsyncSession  # Асинхронная сессия для работы с БД

    @handle_db_errors
    async def get_category_with_words(self, id: int) -> (Category, List[Word]):
        """Получает категорию со всеми словами."""
        result = await self.session.execute(
            select(Category)
            .where(Category.id == id)
            .options(joinedload(Category.words))
        )

        category = result.scalars().first()
        if not category:
            raise NoResultFound()

        words = category.words
        return category, words

    @handle_db_errors
    async def create(
        self, new_data: CreateCategoryWordsSchema
    ) -> (Category, List[Word]):
        """Создает новую категорию со словами в базе данных."""
        # TODO

    #
    # @handle_db_errors
    # async def update(
    #     self,
    #     update_data: UpdateCategorySchema,
    # ) -> Category:
    #     """Обновляет существующую категорию."""
    #     data = await self.get_by_id(update_data.id)
    #     if not data:
    #         raise NoResultFound()
    #
    #     for key, value in update_data.model_dump().items():
    #         setattr(data, key, value)
    #
    #     await self.session.commit()
    #     await self.session.refresh(data)
    #
    #     return data
    #
    # @handle_db_errors
    # async def delete(self, id: int):
    #     """Удаляет категорию из базы данных."""
    #     data = await self.get_by_id(id)
    #     if not data:
    #         raise NoResultFound()
    #
    #     await self.session.delete(data)
    #     await self.session.commit()
