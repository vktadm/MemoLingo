from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


from api.schemas import CreateUserWordSchema, UserWordSchema
from database import Word, UserWord


async def get_new_user_words(
    session: AsyncSession,
    user_id: int,
    quantity_words: int,
    category: str = None,
) -> list[Word] | None:
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
    user_id: int,
    session: AsyncSession,
    new_words: list[CreateUserWordSchema],
) -> list[UserWord]:
    """Создает UserWord для каждого слова."""
    words = [
        UserWord(**new_word.model_dump(), user_id=user_id) for new_word in new_words
    ]
    session.add_all(words)
    await session.commit()
    return list(words)
