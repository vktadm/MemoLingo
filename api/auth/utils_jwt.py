import jwt
from datetime import timedelta, datetime

from core.config import settings


def encode_jwt(
    payload: dict,
    key: str = settings.auth_jwt.secret,
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    expire = now + timedelta(minutes=expire_minutes)

    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(payload, key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    key: str = settings.auth_jwt.secret,
    algorithm: str = settings.auth_jwt.algorithm,
):
    decoded = jwt.decode(jwt=token, key=key, algorithms=algorithm)
    return decoded
