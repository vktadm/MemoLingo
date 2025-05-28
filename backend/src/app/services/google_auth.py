from dataclasses import dataclass

from backend.src.app.clients import GoogleClient
from backend.src.app.repository.black_list import TokenBlackListRepository
from backend.src.app.schemas import UserLoginSchema, UserSchema, GoogleUserDataSchema
from backend.src.app.repository import UsersRepository
from backend.src.app.services import JWTService


@dataclass
class GoogleAuthService:
    user_repository: UsersRepository
    google_client: GoogleClient
    jwt_service: JWTService
    black_list: TokenBlackListRepository

    async def auth_google(self, code: str) -> UserLoginSchema:
        """Аутентификация через Google OAuth."""
        # TODO Ошибки
        user_data = await self.google_client.get_user_info(code)
        user = await self._get_or_create_google_user(user_data)
        return await self._generate_auth_response(user)

    async def get_google_redirect_url(self) -> str:
        """Получает URL для перенаправления на Google OAuth."""
        return self.google_client.settings.get_url

    async def _generate_auth_response(self, user: UserSchema) -> UserLoginSchema:
        """Генерирует ответ с токеном для аутентифицированного пользователя."""
        access_token = self._create_access_token(user)
        await self._store_token(access_token)
        return UserLoginSchema(access_token=access_token, id=user.id)

    async def _get_or_create_google_user(
        self, user_data: GoogleUserDataSchema
    ) -> UserSchema:
        """Получает или создает пользователя для Google auth."""
        user = await self.user_repository.get_user_by_email(user_data.email)
        if user:
            return UserSchema.model_validate(user)
        new_user = await self.user_repository.create_google_user(
            **user_data.model_dump()
        )
        return UserSchema.model_validate(new_user)

    async def _store_token(self, token: str):
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
