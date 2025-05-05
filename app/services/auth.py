from dataclasses import dataclass
from typing import Optional
from jwt import ExpiredSignatureError, PyJWTError

from app.clients import GoogleClient
from app.exceptions import UserNoCreate, TokenExpired, TokenException
from app.repository.black_list import TokenBlackListRepository
from app.schemas import UserLoginSchema
from app.repository import UsersRepository
from app.exceptions import UserNotFound, UserIncorrectPassword
from app.services.crypto_manager import CryptoService
from app.services.jwt_manager import JWTService


@dataclass
class AuthService:
    user_repository: UsersRepository
    jwt_service: JWTService
    crypto_service: CryptoService
    black_list: TokenBlackListRepository

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

    async def _validate_user_credentials(self, username: str, password: str):
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

    async def _generate_auth_response(self, user) -> UserLoginSchema:
        """Генерирует ответ с токеном для аутентифицированного пользователя."""
        access_token = self._create_access_token(user)
        await self._store_token(access_token)
        return UserLoginSchema(access_token=access_token)

    async def _store_token(self, token: str):
        """Сохраняет токен с указанием времени жизни."""
        await self.black_list.add_token(
            token,
            self.jwt_service.settings.access_token_expire_minutes,
        )

    def _create_access_token(self, user) -> str:
        """Создает JWT токен."""
        jwt_payload = {
            "sub": user.username,
            "id": user.id,
            "username": user.username,
        }
        return self.jwt_service.encode_jwt(payload=jwt_payload)

    # async def login(
    #     self,
    #     username: str,
    #     password: str,
    # ) -> Optional[UserLoginSchema]:
    #     """Авторизация по login и password."""
    #     user = await self.user_repository.get_user_by_username(username=username)
    #     if not user or not user.password:
    #         raise exceptions.UserNotFound
    #
    #     if not self.crypto_service.validate_password(
    #         password=password,
    #         hashed_password=user.password,
    #     ):
    #         raise exceptions.UserIncorrectPassword
    #
    #     access_token = self.get_access_token(
    #         user_id=user.id,
    #         username=user.username,
    #     )
    #
    #     await self.black_list.add_token(
    #         access_token,
    #         self.jwt_service.settings.access_token_expire_minutes,
    #     )
    #     return UserLoginSchema(access_token=access_token)
    #
    # def get_access_token(self, user_id: int, username: str) -> str:
    #     """Получает jwt-токен."""
    #     jwt_payload = {
    #         "sub": username,
    #         "id": user_id,
    #         "username": username,
    #     }
    #     # TODO: Ошибки при попытке кодирования?
    #     return self.jwt_service.encode_jwt(payload=jwt_payload)
    #
    # async def auth_google(self, code: str) -> UserLoginSchema:
    #     """Авторизация Google."""
    #     user_data = await self.google_client.get_user_info(code)
    #     user = await self.user_repository.get_user_by_email(user_data.email)
    #     if not user:
    #         try:
    #             user = await self.user_repository.create_google_user(
    #                 **user_data.model_dump()
    #             )
    #         # TODO: Обработка ошибок
    #         except Exception:
    #             raise UserNoCreate
    #     access_token = self.get_access_token(
    #         user_id=user.id,
    #         username=user.username,
    #     )
    #     await self.black_list.add_token(
    #         access_token,
    #         self.jwt_service.settings.access_token_expire_minutes,
    #     )
    #     return UserLoginSchema(access_token=access_token)
    #
    # def get_google_redirect_url(self) -> str:
    #     return self.google_client.settings.get_url
    #
    # async def get_user_id_by_access_token(self, access_token: str) -> int:
    #     """Получает user_id из access_token."""
    #     if await self.black_list.token_is_expired(access_token):
    #         raise exceptions.TokenException
    #     try:
    #         payload = self.jwt_service.decode_jwt(token=access_token)
    #     except ExpiredSignatureError:
    #         raise exceptions.TokenExpired
    #     except PyJWTError:
    #         raise exceptions.TokenException
    #     return payload["id"]
    #
    # async def get_username_by_access_token(self, access_token: str) -> str:
    #     """Получает username из access_token."""
    #     if await self.black_list.token_is_expired(access_token):
    #         raise exceptions.TokenException
    #     try:
    #         payload = self.jwt_service.decode_jwt(token=access_token)
    #     except ExpiredSignatureError:
    #         raise exceptions.TokenExpired
    #     except PyJWTError:
    #         raise exceptions.TokenException
    #     return payload["username"]
    #
    # async def revoke_token(self, access_token: str) -> str:
    #     """Отзывает токен доступа."""
    #     username = await self.get_username_by_access_token(access_token)
    #     await self.black_list.block_token(access_token)
    #     return username
