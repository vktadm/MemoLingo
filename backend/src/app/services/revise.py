from sqlalchemy import select, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


from backend.src.app.database import Category, UserWord, Status


async def get_user_words(
    session: AsyncSession,
    user_id: int,
    category: str = None,
) -> list[Category] | None:
    """
    Получает все слова, которых с UserProgress.status == NotStudy.
    TODO category - категория, из которой берем слова для повторения.
    """
    stmt = select(Category).where(
        Category.id.in_(
            select(UserWord.word_id).where(
                UserWord.user_id == user_id,
                UserWord.status == Status.revise,
            )
        )
    )

    result: Result = await session.execute(stmt)
    words = result.scalars().all()
    return list(words)


async def get_random_words(
    session: AsyncSession,
    word_id: int,
) -> list[str]:

    stmt = (
        select(Category).where(Category.id != word_id).order_by(func.random()).limit(3)
    )
    result: Result = await session.execute(stmt)
    words = result.scalars().all()

    return list(words)
