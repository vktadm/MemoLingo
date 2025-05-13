import jwt
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta

from backend.app.decorators import handle_jwt_manager_errors
from backend.app.settings import JWTSettings


@dataclass
class JWTService:
    """Сервис для работы с JWT (JSON Web Tokens)."""

    settings: JWTSettings  # Конфигурация JWT из настроек приложения

    def encode_jwt(self, payload: dict):
        """Генерирует JWT токен на основе полезной нагрузки."""
        to_encode = payload.copy()
        now = datetime.now(timezone.utc)
        expire = now + timedelta(minutes=self.settings.access_token_expire_minutes)
        to_encode.update(exp=expire, iat=now)
        encoded = jwt.encode(
            payload=to_encode,
            key=self.settings.secret,
            algorithm=self.settings.algorithm,
        )
        return encoded

    @handle_jwt_manager_errors
    def decode_jwt(self, token: str):
        """Валидирует и декодирует JWT токен."""
        decoded = jwt.decode(
            jwt=token,
            key=self.settings.secret,
            algorithms=self.settings.algorithm,
        )
        return decoded
