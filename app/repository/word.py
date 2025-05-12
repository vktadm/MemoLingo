from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound


from app.database import Word
from app.decorators import handle_db_errors
from app.schemas.word import CreateWordSchema, UpdateWordSchema


@dataclass
class WordRepository:
    """
    Класс-репозиторий для работы с моделью Word в базе данных.
    Реализует CRUD (Create, Read, Update, Delete) операции.
    Использует асинхронный SQLAlchemy для работы с БД.
    """

    session: AsyncSession  # Асинхронная сессия для работы с БД

    @handle_db_errors
    async def get_all(self) -> Optional[List[Word]]:
        """Получает все существующие слова из базы данных."""
        stmt = select(Word).order_by(Word.wrd)
        result: Result = await self.session.execute(stmt)

        return list(result.scalars().all())

    @handle_db_errors
    async def get_by_id(self, id: int) -> Optional[Word]:
        """Получает слово по его идентификатору."""
        return await self.session.get(Word, id)

    @handle_db_errors
    async def get_by_wrd(
        self,
        wrd: str,
    ) -> Optional[Word]:
        """Получает слово по его значению."""
        stmt = select(Word).where(Word.wrd == wrd)

        return await self.session.scalar(stmt)

    @handle_db_errors
    async def create(self, new_data: CreateWordSchema) -> Word:
        """Создает новое слово в базе данных."""
        data = Word(**new_data.model_dump())
        self.session.add(data)
        await self.session.commit()
        await self.session.flush()

        return data

    @handle_db_errors
    async def update(
        self,
        update_data: UpdateWordSchema,
    ) -> Word:
        """Обновляет существующее слово."""
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
        data = await self.get_by_id(id)
        if not data:
            raise NoResultFound()

        await self.session.delete(data)
        await self.session.commit()
