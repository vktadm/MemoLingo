from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


from .schemas import NewUserWord

from core.models import Word, UserProgress, User


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
    user = await user_by_id(user_id=user_id, session=session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: User {user_id} not found!",
        )

    stmt = (
        select(Word)
        .where(
            Word.id.notin_(
                select(UserProgress.word_id).where(UserProgress.user_id == user_id)
            )
        )
        .limit(quantity_words)
    )

    result: Result = await session.execute(stmt)
    user_words = result.scalars().all()

    return list(user_words)


async def add_new_user_words(
    session: AsyncSession,
    user_id: int,
    new_words: list[NewUserWord],
) -> list[UserProgress]:
    """Создает UserProgress для каждого слова."""

    # TODO Что будет если 1 слово?
    words = [
        UserProgress(user_id=user_id, word_id=new_word.id, status=new_word.status)
        for new_word in new_words
    ]

    try:
        session.add_all(words)
        await session.commit()
    except IntegrityError as e:
        # Обработка ошибок целостности (например, дубликаты)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"ERROR: Integrity error. Description: {e}",
        )
    except SQLAlchemyError as e:
        # Обработка других ошибок SQLAlchemy
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"ERROR: Couldn't insert data. Description: {e}",
        )

    return list(words)
