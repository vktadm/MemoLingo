from dataclasses import dataclass
from typing import Optional
from jwt import ExpiredSignatureError, PyJWTError

from api.clients import GoogleClient
from api.exceptions import UserNoCreate
from api.repository.black_list import TokenBlackListRepository
from api.schemas import UserLoginSchema
from api.repository import UsersRepository
from api import exceptions
from api.services.crypto import CryptoService
from api.services.jwt import JWTService


@dataclass
class AuthService:
    user_repository: UsersRepository
    google_client: GoogleClient
    jwt_service: JWTService
    crypto_service: CryptoService
    black_list: TokenBlackListRepository

    async def login(
        self,
        username: str,
        password: str,
    ) -> Optional[UserLoginSchema]:
        """Авторизация по login и password."""
        user = await self.user_repository.get_user_by_username(username=username)
        if not user:
            raise exceptions.UserNotFound

        if not user.password:
            raise exceptions.UserNotFound

        if not self.crypto_service.validate_password(
            password=password,
            hashed_password=user.password,
        ):
            raise exceptions.UserIncorrectPassword

        access_token = self._get_access_token(
            user_id=user.id,
            username=user.username,
        )

        await self.black_list.add_token(
            access_token,
            self.jwt_service.settings.access_token_expire_minutes,
        )
        return UserLoginSchema(access_token=access_token)

    def _get_access_token(self, user_id: int, username: str) -> str:
        """Получает jwt-токен."""
        jwt_payload = {
            "sub": username,
            "id": user_id,
            "username": username,
        }
        # TODO: Ошибки при попытке кодирования?
        return self.jwt_service.encode_jwt(payload=jwt_payload)

    async def auth_google(self, code: str) -> UserLoginSchema:
        """Авторизация Google."""
        user_data = self.google_client.get_user_info(code)
        user = await self.user_repository.get_user_by_email(user_data.email)
        if not user:
            try:
                user = await self.user_repository.create_google_user(
                    **user_data.model_dump()
                )
            except Exception:
                raise UserNoCreate
        access_token = self._get_access_token(
            user_id=user.id,
            username=user.username,
        )
        await self.black_list.add_token(
            access_token,
            self.jwt_service.settings.access_token_expire_minutes,
        )
        return UserLoginSchema(access_token=access_token)

    async def get_google_redirect_url(self) -> str:
        return self.google_client.settings.get_url

    async def get_user_id_by_access_token(self, access_token: str) -> int:
        """Получает user из access_token."""
        if await self.black_list.token_is_expired(access_token):
            raise exceptions.TokenException
        try:
            payload = self.jwt_service.decode_jwt(token=access_token)
        except ExpiredSignatureError:
            raise exceptions.TokenExpired
        except PyJWTError:
            raise exceptions.TokenException
        return payload["id"]

    async def get_username_by_access_token(self, access_token: str) -> str:
        if await self.black_list.token_is_expired(access_token):
            raise exceptions.TokenException
        try:
            payload = self.jwt_service.decode_jwt(token=access_token)
        except ExpiredSignatureError:
            raise exceptions.TokenExpired
        except PyJWTError:
            raise exceptions.TokenException
        return payload["username"]

    async def logout(self, access_token: str) -> str:
        """Аннулирует токен доступа."""
        username = await self.get_username_by_access_token(access_token)
        await self.black_list.block_token(access_token)
        return username
