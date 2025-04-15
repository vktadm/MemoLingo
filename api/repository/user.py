from dataclasses import dataclass

from sqlalchemy import select, insert, Result
from sqlalchemy.ext.asyncio import AsyncSession

from database import User


@dataclass
class UsersRepository:
    """CRUD функции для модели User."""

    session: AsyncSession

    async def get_users(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        result: Result = await self.session.execute(stmt)
        words = result.scalars().all()
        return list(words)

    async def get_user(
        self,
        user_id: int = None,
        username: str = None,
    ) -> User | None:
        """Получает User по user_id или username."""
        if user_id:
            return await self.session.get(User, user_id)
        elif username:
            stmt = select(User).where(User.username == username)
            user = await self.session.scalar(stmt)
            print(user)
            return user
        return None

    async def create_user(
        self,
        username: str,
        password: str,
        # email: EmailStr = Form(default=None),
    ) -> User | None:
        """Создает User."""
        # TODO: Обработка ошибок
        user = User(username=username, password=password)
        self.session.add(user)
        await self.session.commit()
        return user
