from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.app.database import User
from backend.src.app.decorators import handle_db_errors


@dataclass
class UsersRepository:
    """CRUD функции для модели User."""

    session: AsyncSession

    @handle_db_errors
    async def get_users(self) -> List[User]:
        """Получает всех существующих пользователей."""
        print(self.session)
        stmt = select(User).order_by(User.id)
        result: Result = await self.session.execute(stmt)
        words = result.scalars().all()
        return list(words)

    @handle_db_errors
    async def get_user_by_id(
        self,
        user_id: int,
    ) -> Optional[User]:
        """Получает User по user_id или username."""
        return await self.session.get(User, user_id)

    @handle_db_errors
    async def get_user_by_username(
        self,
        username: str,
    ) -> Optional[User]:
        """Получает User по username."""
        stmt = select(User).where(User.username == username)
        return await self.session.scalar(stmt)

    @handle_db_errors
    async def get_user_by_email(
        self,
        email: str,
    ) -> Optional[User]:
        """Получает User по email."""
        stmt = select(User).where(User.email == email)
        return await self.session.scalar(stmt)

    @handle_db_errors
    async def create_user(
        self,
        username: str,
        password: str,
        email: Optional[str] = None,
    ) -> User:
        """Создает User."""
        user = User(
            username=username,
            password=password,
            email=email,
        )
        self.session.add(user)
        await self.session.commit()
        return user

    @handle_db_errors
    async def create_google_user(
        self,
        username: str,
        google_access_token: str,
        name: Optional[str] = None,
        email: Optional[str] = None,
        is_active: bool = True,
    ) -> User:
        """Создает User с google_access_token."""
        user = User(
            username=username,
            google_access_token=google_access_token,
            name=name,
            email=email,
            is_active=is_active,
        )
        self.session.add(user)
        await self.session.commit()
        return user
