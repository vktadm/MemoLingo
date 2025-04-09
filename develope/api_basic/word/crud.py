from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from database import Word

from api.schemas.word import WordCreate, WordUpdate


async def get_words(session: AsyncSession) -> list[Word]:
    stmt = select(Word).order_by(Word.wrd)
    result: Result = await session.execute(stmt)
    words = result.scalars().all()
    return list(words)


async def get_word(session: AsyncSession, word_id: int) -> Word | None:
    return await session.get(Word, word_id)


async def create_word(session: AsyncSession, word_in: WordCreate) -> Word:
    word = Word(**word_in.model_dump())
    session.add(word)
    await session.commit()
    # await session.refresh(product)
    return word


async def update_word(
    session: AsyncSession,
    word: Word,
    word_update: WordUpdate,
    partial: bool = False,
) -> Word | None:

    for key, value in word_update.model_dump(exclude_unset=partial).items():
        setattr(word, key, value)
    await session.commit()

    return word


async def delete_word(
    session: AsyncSession,
    word: Word,
) -> None:
    await session.delete(word)
    await session.commit()
