from dataclasses import dataclass
from typing import Optional
from jwt import ExpiredSignatureError, PyJWTError

from app.exceptions import TokenExpired, TokenException
from app.repository.black_list import TokenBlackListRepository
from app.schemas import UserLoginSchema, UserSchema
from app.repository import UsersRepository
from app.exceptions import UserNotFound, UserIncorrectPassword
from app.services.crypto_manager import CryptoService
from app.services.jwt_manager import JWTService


@dataclass
class AuthService:
    """Сервис аутентификации и управления пользовательскими сессиями."""

    user_repository: UsersRepository  # Работа с БД пользователей
    jwt_service: JWTService  # Генерация токенов
    crypto_service: CryptoService  # Проверка паролей
    black_list: TokenBlackListRepository  # Хранение активных и неактивных токенов

    async def login(self, username: str, password: str) -> UserLoginSchema:
        """Аутентификация пользователя по логину и паролю."""
        user = await self._validate_user_credentials(username, password)
        return await self._generate_auth_response(user)

    async def validate_access_token(self, access_token: str) -> dict:
        """Валидирует access token и возвращает payload."""
        if await self.black_list.token_is_expired(access_token):
            raise TokenException

        try:
            return self.jwt_service.decode_jwt(token=access_token)
        except ExpiredSignatureError:
            raise TokenExpired
        except PyJWTError:
            raise TokenException

    async def revoke_token(self, access_token: str) -> str:
        """Отзывает токен доступа."""
        payload = await self.validate_access_token(access_token)
        await self.black_list.block_token(access_token)
        return payload["username"]

    async def _validate_user_credentials(
        self, username: str, password: str
    ) -> Optional[UserSchema]:
        """Валидация учетных данных пользователя."""
        user = await self.user_repository.get_user_by_username(username=username)

        if not user or not user.password:
            raise UserNotFound

        if not self.crypto_service.validate_password(
            password=password,
            hashed_password=user.password,
        ):
            raise UserIncorrectPassword
        return user

    async def _generate_auth_response(self, user: UserSchema) -> UserLoginSchema:
        """Генерирует ответ с токеном для аутентифицированного пользователя."""
        access_token = self._create_access_token(user)
        await self._store_token(access_token)
        return UserLoginSchema(access_token=access_token, id=user.id)

    async def _store_token(self, token: str) -> None:
        """Сохраняет токен с указанием времени жизни."""
        await self.black_list.add_token(token)

    def _create_access_token(self, user: UserSchema) -> str:
        """Создает JWT токен."""
        jwt_payload = {
            "sub": user.username,
            "id": user.id,
            "username": user.username,
        }
        return self.jwt_service.encode_jwt(payload=jwt_payload)
