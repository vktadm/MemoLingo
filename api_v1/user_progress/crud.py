from sqlalchemy import select, insert
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import UserProgress

from .schemas import UserWord


async def get_user_progress(
    session: AsyncSession,
    user_id,
) -> list[UserProgress]:
    stmt = select(UserProgress).where(UserProgress.user_id == user_id)
    result: Result = await session.execute(stmt)
    user_words = result.scalars().all()
    return list(user_words)


async def add_words_to_user_progress(
    session: AsyncSession, words: list[UserWord]
) -> list[UserProgress]:
    user_words = [UserProgress(**word.model_dump()) for word in words]
    session.add_all(user_words)
    await session.commit()
    return list(user_words)


async def change_user_words_status(
    session: AsyncSession,
    words: list[UserWord],
) -> list[UserProgress]:
    for word in words:
        for key, value in word.model_dump(exclude_unset=True).items():
            setattr(word, key, value)
    await session.commit()
    session.add_all(user_words)
    await session.commit()
    return list(user_words)
