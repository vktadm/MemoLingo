import asyncio

from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

# from sqlalchemy.engine import Result
from database import db_helper, User, Category, Word


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print(f"NEW USER: {user}")
    return user


async def get_user(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    # result: Result = await session.execute(stmt)
    # user: User | None = result.scalar_one_or_none()
    user: User | None = await session.scalar(stmt)

    # используем если уверены, что существует элемент
    # user: User | None = result.scalar_one()

    print(f"USER BY USERNAME: {username} -> {user}")
    return user


async def create_category(
    session: AsyncSession, title: str, translation: str
) -> Category:
    category = Category(title=title, translation=translation)
    session.add(category)
    await session.commit()
    print(f"NEW CATEGORY: {category}")
    return category


async def create_words(session: AsyncSession, wrd, translation) -> Word:
    word = Word(wrd=wrd, translation=translation)
    session.add(word)
    await session.commit()
    print(f"NEW WORD: {word}")
    return word


async def get_category_with_words(session: AsyncSession, title) -> Category:
    category = await session.scalar(
        select(Category)
        .where(Category.title == title)
        .options(selectinload(Category.words))
    )
    await session.commit()
    return category


async def main():
    async with db_helper.session_factory() as session:
        category = await create_category(session, "body", "тело")
        data = [
            {"wrd": "body", "translation": "тело"},
            {"wrd": "head", "translation": "голова"},
            {"wrd": "shoulder", "translation": "плечо"},
        ]
        words = []
        for itm in data:
            words.append(await create_words(session, **itm))

        category = await get_category_with_words(session=session, title=category.title)
        category.words.extend(words)
        await session.commit()

        category = await get_category_with_words(session=session, title="body")
        print(str(category))
        for itm in category.words:
            print(itm.wrd, itm.translation, itm.transcription)


if __name__ == "__main__":
    asyncio.run(main())
