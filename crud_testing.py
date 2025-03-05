import asyncio
from sqlalchemy import select, insert

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

# from sqlalchemy.engine import Result
from core.models import db_helper, User, Category, Word, CategoryWord


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


async def main():
    async with db_helper.session_factory() as session:
        # category_title = "general"
        # category_translation = "основное"
        # data = [
        #     {"wrd": "house", "translation": "дом"},
        #     {"wrd": "apple", "translation": "яблоко"},
        #     {"wrd": "bread", "translation": "хлеб"},
        #     {"wrd": "hello", "translation": "привет"},
        # ]
        # category = await create_category(
        #     session=session,
        #     title=category_title,
        #     translation=category_translation,
        # )
        # words = []
        # for itm in data:
        #     words.append(
        #         await create_words(
        #             session,
        #             wrd=itm["wrd"],
        #             translation=itm["translation"],
        #         )
        #     )
        # print(words)
        category = await session.get(
            Category, 1, options=(selectinload(Category.words),)
        )
        print(category)
        word = await session.get(Word, 1)
        category.words = [
            word,
        ]
        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())

# from sqlalchemy import select
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine
# from core.models import UserProgress
#
#
# engine = create_engine("sqlite:///db.sqlite3", echo=True)
# session = Session(engine)
#
# stmt = select(UserProgress)
#
# result = session.execute(stmt)
# users = result.scalars().all()
#
# for user in users:
#     print(user.id, user.status.value, user.t_stamp)
