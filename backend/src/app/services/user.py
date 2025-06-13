from dataclasses import dataclass

from backend.src.app.exceptions import (
    NotFoundException,
    UserAlreadyExistsException,
    SMTPException,
)
from backend.src.app.repository import UsersRepository
from backend.src.app.schemas import UserSchema, UserCreateSchema
from backend.src.app.services.crypto_manager import CryptoService


@dataclass
class UserService:
    """Сервис для управления пользователями."""

    user_repository: UsersRepository  # Доступ к данным пользователей в БД
    crypto_service: CryptoService  # Хеширование и проверка паролей

    async def create_user(
        self,
        user_create: UserCreateSchema,
    ) -> UserSchema:
        """Создает нового пользователя в системе."""
        user_create.password = self.crypto_service.hash_password(user_create.password)
        if await self.user_repository.get_user_by_username(
            username=user_create.username
        ):
            raise UserAlreadyExistsException()

        db_user = await self.user_repository.create_user(**user_create.model_dump())

        return UserSchema.model_validate(db_user)

    async def get_users(self) -> list[UserSchema]:
        """Получает список всех пользователей."""
        db_users = await self.user_repository.get_users()
        users = [UserSchema.model_validate(itm) for itm in db_users]
        if not users:
            raise NotFoundException()

        return users

    async def get_user_by_id(self, user_id: int) -> UserSchema:
        """Получает пользователя по его идентификатору."""
        db_user = await self.user_repository.get_user_by_id(user_id=user_id)
        user = UserSchema.model_validate(db_user)
        if not user:
            raise NotFoundException()

        return user
