import jwt
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta

from app.config import JWTSettings


@dataclass
class JWTService:
    settings: JWTSettings

    def encode_jwt(self, payload: dict):
        """Кодирование JWT."""
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

    def decode_jwt(self, token: str):
        """Декодирование JWT."""
        decoded = jwt.decode(
            jwt=token,
            key=self.settings.secret,
            algorithms=self.settings.algorithm,
        )
        return decoded
