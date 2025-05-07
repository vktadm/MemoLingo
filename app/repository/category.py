from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.database import Category
from app.decorators import handle_db_errors
from app.schemas import CreateCategorySchema, UpdateCategorySchema


@dataclass
class CategoryRepository:
    """
    Класс-репозиторий для работы с моделью Category в базе данных.
    Реализует CRUD (Create, Read, Update, Delete) операции.
    Использует асинхронный SQLAlchemy для работы с БД.
    """

    session: AsyncSession  # Асинхронная сессия для работы с БД

    @handle_db_errors
    async def get_categories(self) -> Optional[List[Category]]:
        """Получает все существующие категории из базы данных."""
        stmt = select(Category).order_by(Category.title)
        result: Result = await self.session.execute(stmt)
        categories = result.scalars().all()

        return list(categories)

    @handle_db_errors
    async def get_category(
        self,
        title: str,
    ) -> Optional[Category]:
        """Получает каткгорию по ее значению."""
        stmt = select(Category).where(Category.title == title)

        return await self.session.scalar(stmt)

    @handle_db_errors
    async def get_category_by_id(
        self,
        category_id: int,
    ) -> Optional[Category]:
        """Получает категорию по ее идентификатору."""
        return await self.session.get(Category, category_id)

    @handle_db_errors
    async def create_category(
        self,
        new_category: CreateCategorySchema,
        icon: str = None,
    ) -> Category:
        """Создает новую категорию в базе данных."""
        category = Category(**new_category.model_dump(), icon=icon)
        self.session.add(category)
        await self.session.commit()

        return await self.get_category(new_category.title)

    @handle_db_errors
    async def update_category(
        self,
        category_id: int,
        update_category: UpdateCategorySchema,
    ) -> Category:
        """Обновляет существующую категорию."""
        category_db = await self.get_category_by_id(category_id)
        if not category_db:
            raise NoResultFound()

        update_data = update_category.model_dump()
        for key, value in update_data.items():
            setattr(category_db, key, value)

        await self.session.commit()
        await self.session.refresh(category_db)

        return category_db

    @handle_db_errors
    async def delete_category(self, category_id: int) -> bool:
        """Удаляет категорию из базы данных."""
        category = await self.get_category_by_id(category_id)
        if not category:
            raise NoResultFound()

        await self.session.delete(category)
        await self.session.commit()

        return True
