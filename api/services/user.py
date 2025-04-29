from dataclasses import dataclass
from typing import Optional

from api.exceptions import UserAlreadyExists, UserNoCreate
from api.exceptions.base import NoContent
from api.repository import UsersRepository
from api.schemas import UserSchema
from api.services.crypto import CryptoService


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
