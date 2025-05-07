from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession


from app.database import Word
from app.exceptions import NotFound
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
    async def get_words(self) -> Optional[List[Word]]:
        """Получает все существующие слова из базы данных."""
        stmt = select(Word).order_by(Word.wrd)
        result: Result = await self.session.execute(stmt)
        words = result.scalars().all()

        return list(words)

    @handle_db_errors
    async def get_word(
        self,
        wrd: str,
    ) -> Optional[Word]:
        """Получает слово по его значению."""
        stmt = select(Word).where(Word.wrd == wrd)

        return await self.session.scalar(stmt)

    @handle_db_errors
    async def get_word_by_id(
        self,
        word_id: int,
    ) -> Optional[Word]:
        """Получает слово по его идентификатору."""
        return await self.session.get(Word, word_id)

    @handle_db_errors
    async def create_word(self, new_word: CreateWordSchema) -> Word:
        """Создает новое слово в базе данных."""
        self.session.add(new_word)
        await self.session.commit()

        return await self.get_word(new_word.wrd)

    @handle_db_errors
    async def update_word(
        self,
        word_id: int,
        update_word: UpdateWordSchema,
    ) -> Word:
        """Обновляет существующее слово."""
        word_db = await self.get_word_by_id(word_id)
        if not word_db:
            raise NotFound

        update_data = update_word.model_dump()
        for key, value in update_data.items():
            setattr(word_db, key, value)

        await self.session.commit()
        await self.session.refresh(word_db)

        return word_db

    @handle_db_errors
    async def delete_word(self, word_id: int) -> bool:
        """Удаляет слово из базы данных."""
        word = await self.get_word_by_id(word_id)
        if not word:
            raise NotFound

        await self.session.delete(word)
        await self.session.commit()

        return True
