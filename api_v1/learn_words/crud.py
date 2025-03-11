from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from ..word.schemas import Word as WordSchema
from ..user_progress.schemas import UserWord as UserWordSchema
from core.models import Word, UserProgress, Status


async def get_new_user_words(
    session: AsyncSession,
    user_id: int,
    quantity_words: int,
) -> list[Word]:
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
    # TODO: Проверка на существование слов
    return list(user_words)


async def add_new_user_words(
    session: AsyncSession,
    user_id: int,
    words_in: list[Word],
) -> list[UserProgress]:
    words = [
        UserProgress(user_id=user_id, word_id=word.id, status=Status.NotStudy)
        for word in words_in
    ]
    session.add_all(words)
    await session.commit()
    return list(words)
