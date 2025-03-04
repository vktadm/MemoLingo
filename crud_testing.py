import asyncio
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

# from sqlalchemy.engine import Result
from core.models import db_helper, User, Category, Word


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


async def create_category(session: AsyncSession, title: str) -> Category:
    category = Category(title=title)
    session.add(category)
    await session.commit()
    print(f"NEW CATEGORY: {category}")
    return category


async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, username="victoria")
        # await create_user(session=session, username="bob")
        # await create_user(session=session, username="tom")
        # await get_user(session=session, username="tom")
        pass


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
