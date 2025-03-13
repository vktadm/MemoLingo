from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


from .schemas import UserWord
from core.models import Word, UserProgress, User, Status


async def user_by_id(
    user_id: int,
    session: AsyncSession,
) -> User | None:
    """Проверяет существование пользователя в БД."""

    user = await session.get(User, user_id)

    return user


async def get_user_words(
    session: AsyncSession,
    user_id: int,
    category: str = None,
) -> list[UserWord]:
    """
    Получает все слова, которых с UserProgress.status == NotStudy.
    TODO category - категория, из которой берем слова для повторения.
    """
    stmt = select(Word).where(
        Word.id.in_(
            select(UserProgress.word_id).where(
                UserProgress.user_id == user_id,
                UserProgress.status == Status.NotStudy,
            )
        )
    )

    result: Result = await session.execute(stmt)
    words = result.scalars().all()

    user_words = [UserWord() for word in words]

    return list(user_words)


async def get_random_words(
    session: AsyncSession,
    word_id: int,
) -> list[str]:

    stmt = select(Word.wrd).where(Word.id != word_id).order_by(func.random()).limit(3)
    result: Result = await session.execute(stmt)
    words = result.scalars().all()

    return list(words)
