import logging
from typing import Optional

import jwt
from jwt import PyJWTError
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta

from backend.src.app.settings import JWTSettings

logger = logging.getLogger(__name__)


@dataclass
class JWTService:
    """Сервис для работы с JWT (JSON Web Tokens)."""

    settings: JWTSettings  # Конфигурация JWT из настроек приложения

    def encode_jwt(self, payload: dict) -> Optional[str]:
        """Генерирует JWT токен на основе полезной нагрузки."""
        to_encode = payload.copy()
        now = datetime.now(timezone.utc)
        expire = now + timedelta(minutes=self.settings.access_token_expire_minutes)
        to_encode.update(exp=expire, iat=now)
        try:
            encoded = jwt.encode(
                payload=to_encode,
                key=self.settings.secret,
                algorithm=self.settings.algorithm,
            )
            return encoded
        except PyJWTError as e:
            logger.info(f"Try yo encode payload : {payload}. Error detail: {e}.")

    def decode_jwt(self, token: str) -> Optional[dict]:
        """Валидирует и декодирует JWT токен."""
        try:
            decoded = jwt.decode(
                jwt=token,
                key=self.settings.secret,
                algorithms=self.settings.algorithm,
            )
            return decoded
        except PyJWTError as e:
            logger.info(f"Try yo decode invalid jwt token: {token}. Error detail: {e}.")
            return None
