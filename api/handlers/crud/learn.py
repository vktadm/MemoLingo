from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


from api.schemas.user_word import CreateUserWord
from api.schemas.word import Word
from core.models import Word, UserWord, User


async def user_by_id(
    user_id: int,
    session: AsyncSession,
) -> User | None:
    """Проверяет существование пользователя в БД."""

    user = await session.get(User, user_id)
    return user


async def get_new_user_words(
    session: AsyncSession,
    user_id: int,
    quantity_words: int,
    category: str = None,
) -> list[Word]:
    """
    Получает {quantity_words} слов, которых нет в UserProgress.

    quantity_words - кол-во новых слов.
    TODO category - категория, из которой берем слова для изучения.

    TODO В дальнейшем можно создать сущность UserSettings,
    где пользователь сможет настраивать кол-во слов
    для ежедневного изучения.
    """
    stmt = (
        select(Word)
        .where(
            Word.id.notin_(select(UserWord.word_id).where(UserWord.user_id == user_id))
        )
        .limit(quantity_words)
    )

    result: Result = await session.execute(stmt)
    user_words = result.scalars().all()

    return list(user_words)


async def add_new_user_words(
    session: AsyncSession,
    user_id: int,
    new_words: list[CreateUserWord],
) -> list[UserWord]:
    """Создает UserWord для каждого слова."""

    # TODO Что будет если 1 слово?
    words = [UserWord(**new_word.model_dump()) for new_word in new_words]

    session.add_all(words)
    await session.commit()

    return list(words)
