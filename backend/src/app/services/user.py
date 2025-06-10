import secrets
from dataclasses import dataclass
from datetime import datetime, timedelta

from backend.src.app.clients.yandex import SMTPYandexClient
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
        # await self.send_confirmation_email(user_create.email)

        return UserSchema.model_validate(db_user)

    # async def send_confirmation_email(self, email_to: str):
    #     token: str = await self._get_confirmation_token(email_to=email_to)
    #     confirmation_url = f"{self.smtp_client.settings.REDIRECT_URL}?token={token}"
    #     if not await self.smtp_client.send_email(
    #         email_to=email_to,
    #         confirmation_url=confirmation_url,
    #     ):
    #         raise SMTPException()
    #
    # async def verify_confirmation_email(self, token: str):
    #     email = await self.cache.check_token(token)
    #     if not email:
    #         raise ConfirmTokenException()
    #
    #     await self.user_repository.activate(email)
    #
    # async def _get_confirmation_token(self, email_to: str) -> str:
    #     token = secrets.token_urlsafe(10)
    #     await self.cache.add_token(token=token, email=email_to)
    #
    #     return token

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
