from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from backend.app.database import Category
from backend.app.decorators import handle_db_errors
from backend.app.schemas import CreateCategorySchema, UpdateCategorySchema


@dataclass
class CategoryRepository:
    """
    Класс-репозиторий для работы с моделью Category в базе данных.
    Реализует CRUD (Create, Read, Update, Delete) операции.
    Использует асинхронный SQLAlchemy для работы с БД.
    """

    session: AsyncSession  # Асинхронная сессия для работы с БД

    @handle_db_errors
    async def get_all(self) -> Optional[List[Category]]:
        """Получает все существующие категории из базы данных."""
        stmt = select(Category)
        result: Result = await self.session.execute(stmt)

        return list(result.scalars().all())

    @handle_db_errors
    async def get_by_id(self, id: int) -> Optional[Category]:
        """Получает категорию по ее идентификатору."""
        return await self.session.get(Category, id)

    @handle_db_errors
    async def get_by_title(
        self,
        title: str,
    ) -> Optional[Category]:
        """Получает каткгорию по ее значению."""
        stmt = select(Category).where(Category.title == title)

        return await self.session.scalar(stmt)

    @handle_db_errors
    async def create(self, new_data: CreateCategorySchema) -> Category:
        """Создает новую категорию в базе данных."""
        data = Category(**new_data.model_dump())
        self.session.add(data)
        await self.session.commit()
        await self.session.flush()

        return data

    @handle_db_errors
    async def update(
        self,
        update_data: UpdateCategorySchema,
    ) -> Category:
        """Обновляет существующую категорию."""
        data = await self.get_by_id(update_data.id)
        if not data:
            raise NoResultFound()

        for key, value in update_data.model_dump().items():
            setattr(data, key, value)

        await self.session.commit()
        await self.session.refresh(data)

        return data

    @handle_db_errors
    async def delete(self, id: int):
        """Удаляет категорию из базы данных."""
        data = await self.get_by_id(id)
        if not data:
            raise NoResultFound()

        await self.session.delete(data)
        await self.session.commit()
