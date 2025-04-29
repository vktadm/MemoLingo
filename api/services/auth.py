from dataclasses import dataclass
from typing import Optional
from jwt import ExpiredSignatureError, PyJWTError

from api.clients import GoogleClient
from api.schemas import UserLoginSchema, UserCreateSchema
from api.repository import UsersRepository
from api.services import UserService, CryptoService, JWTService
from api import exceptions


@dataclass
class AuthService:
    user_repository: UsersRepository
    user_service: UserService
    google_client: GoogleClient
    jwt_service: JWTService

    async def login(
        self,
        username: str,
        password: str,
    ) -> Optional[UserLoginSchema]:
        """Авторизация по login и password."""
        user = await self.user_repository.get_user(username=username)
        if not user:
            raise exceptions.UserNotFound
        if not CryptoService.validate_password(
            password=password,
            hashed_password=user.password,
        ):
            raise exceptions.UserIncorrectPassword
        login_user = self.get_login_user(
            user_id=user.id,
            username=user.username,
        )
        return login_user

    def get_login_user(self, user_id: int, username: str) -> UserLoginSchema:
        """Получает jwt-токен."""
        jwt_payload = {
            "sub": username,
            "id": user_id,
            "username": username,
        }
        # TODO: Ошибки при попытке кодирования?
        access_token = self.jwt_service.encode_jwt(payload=jwt_payload)
        return UserLoginSchema(access_token=access_token)

    async def auth_google(self, code: str) -> UserLoginSchema:
        """Авторизация Google."""
        user_data = self.google_client.get_user_info(code)
        new_user = UserCreateSchema(
            username=user_data.email,
            google_access_token=user_data.access_token,
            email=user_data.email,
        )
        user = await self.user_service.create_user(new_user)
        return user

    async def get_google_redirect_url(self) -> str:
        return self.google_client.settings.get_url

    async def get_user_id_by_access_token(self, access_token: str) -> int:
        """Получает user из access_token."""
        try:
            payload = self.jwt_service.decode_jwt(token=access_token)
        except ExpiredSignatureError:
            raise exceptions.TokenExpired
        except PyJWTError:
            raise exceptions.TokenException
        return payload["id"]
