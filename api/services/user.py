from dataclasses import dataclass

from api.services import CryptoService, AuthService
from api.exceptions import UserAlreadyExists, UserNoCreate
from api.repository import UsersRepository
from api.schemas import UserCreateSchema, UserLoginSchema, UserSchema


@dataclass
class UserService:
    user_repository: UsersRepository
    auth_service: AuthService

    async def create_user(
        self,
        new_user: UserCreateSchema,
    ) -> UserLoginSchema:
        hashed_password: str = CryptoService.hash_password(new_user.password)
        if await self.user_repository.get_user(username=new_user.username):
            raise UserAlreadyExists
        new_user.password = hashed_password
        try:
            user = await self.user_repository.create_user(new_user)
        except Exception as e:
            raise UserNoCreate
        login_user = self.auth_service.get_login_user(
            user_id=user.id,
            username=user.username,
        )
        return login_user

    async def get_users(self) -> list[UserSchema]:
        data = await self.user_repository.get_users()
        users = [UserSchema(id=user.id, username=user.username) for user in data]
        return users
