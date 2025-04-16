from dataclasses import dataclass

from api.crypto import Crypto
from api.exceptions import UserAlreadyExists
from api.repository import UsersRepository
from api.schemas import UserLoginSchema, UserSchema
from api.services.auth import AuthService


@dataclass
class UserService:
    user_repository: UsersRepository
    auth_service: AuthService

    async def create_user(
        self,
        username: str,
        password: str,
    ) -> UserLoginSchema:
        hashed_password: str = Crypto.hash_password(password)
        if await self.user_repository.get_user(username=username):
            raise UserAlreadyExists
        user = await self.user_repository.create_user(
            username=username,
            password=hashed_password,
        )
        jwt_payload = {
            "sub": user.username,
            "id": user.id,
            "username": user.username,
        }
        access_token = self.auth_service.encode_jwt(payload=jwt_payload)
        return UserLoginSchema(access_token=access_token)

    async def get_users(self) -> list[UserSchema]:
        data = await self.user_repository.get_users()
        users = [UserSchema(id=user.id, username=user.username) for user in data]
        return users
