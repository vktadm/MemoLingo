from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import User


class UsersRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(
        self,
        user_id: int = None,
        username: str = None,
    ) -> User | None:
        """Получает User по user_id или username"""
        if user_id:
            return await self.session.get(User, user_id)
        if username:
            stmt = select(User).where(User.username == username)
            return await self.session.scalar(stmt)
        return None
