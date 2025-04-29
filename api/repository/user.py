from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import UserCreateSchema
from database import User


@dataclass
class UsersRepository:
    """CRUD функции для модели User."""

    session: AsyncSession

    async def get_users(self) -> List[User]:
        """Получает всех существующих пользователей."""
        stmt = select(User).order_by(User.id)
        result: Result = await self.session.execute(stmt)
        words = result.scalars().all()
        return list(words)

    async def get_user(
        self,
        user_id: int = None,
        username: str = None,
    ) -> Optional[User]:
        """Получает User по user_id или username."""
        if user_id:
            return await self.session.get(User, user_id)
        elif username:
            stmt = select(User).where(User.username == username)
            user = await self.session.scalar(stmt)
            return user
        return None

    async def create_user(self, user_data: UserCreateSchema) -> User:
        """Создает User."""
        # TODO: Обработка ошибок
        user = User(**user_data.model_dump())
        self.session.add(user_data)
        await self.session.commit()
        return user
