from dataclasses import dataclass
from typing import Optional

from app.exceptions import UserAlreadyExists, UserNoCreate
from app.exceptions.base import NoContent
from app.repository import UsersRepository
from app.schemas import UserSchema
from app.services.crypto import CryptoService


@dataclass
class UserService:
    user_repository: UsersRepository
    crypto_service: CryptoService

    async def create_user(
        self,
        username: str,
        password: str,
        email: Optional[str] = None,
    ) -> UserSchema:
        hashed_password = self.crypto_service.hash_password(password)
        if await self.user_repository.get_user_by_username(username=username):
            raise UserAlreadyExists
        try:
            user = await self.user_repository.create_user(
                username=username, password=hashed_password, email=email
            )
        except Exception:
            raise UserNoCreate
        return UserSchema(id=user.id, username=user.username, email=user.email)

    async def get_users(self) -> list[UserSchema]:
        data = await self.user_repository.get_users()
        users = [
            UserSchema(
                id=user.id,
                username=user.username,
                email=user.email,
                name=user.name,
            )
            for user in data
        ]
        if not users:
            raise NoContent
        return users

    async def get_user_by_id(self, user_id: int) -> UserSchema:
        data = await self.user_repository.get_user_by_id(user_id=user_id)
        user = UserSchema(
            id=data.id,
            username=data.username,
            email=data.email,
            name=data.name,
        )
        if not user:
            raise NoContent
        return user
