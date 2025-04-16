from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import jwt
from jwt import ExpiredSignatureError, PyJWTError

from api.exceptions import TokenExpired, TokenException
from api.schemas import UserLoginSchema, UserSchema
from api.repository import UsersRepository
from api.crypto import Crypto
from api import exceptions
from config import settings


@dataclass
class AuthService:
    user_repository: UsersRepository

    async def login(
        self,
        username: str,
        password: str,
    ) -> UserLoginSchema | None:
        """Авторизация с генерацией JWT токена."""
        user = await self.user_repository.get_user(username=username)
        if not user:
            raise exceptions.UserNotFound
        if not Crypto.validate_password(
            password=password,
            hashed_password=user.password,
        ):
            raise exceptions.UserIncorrectPassword
        jwt_payload = {
            "sub": user.username,
            "id": user.id,
            "username": user.username,
        }
        access_token = self.encode_jwt(payload=jwt_payload)
        return UserLoginSchema(access_token=access_token)

    async def get_user_id_by_access_token(self, access_token: str) -> int:
        try:
            payload = self.decode_jwt(token=access_token)
        except ExpiredSignatureError:
            raise TokenExpired
        except PyJWTError:
            raise TokenException
        return payload["id"]

    @staticmethod
    def encode_jwt(
        payload: dict,
        key: str = settings.auth_jwt.secret,
        algorithm: str = settings.auth_jwt.algorithm,
        expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    ):
        """Кодирование JWT."""
        to_encode = payload.copy()
        now = datetime.now(timezone.utc)
        expire = now + timedelta(minutes=expire_minutes)

        to_encode.update(
            exp=expire,
            iat=now,
        )
        encoded = jwt.encode(to_encode, key, algorithm=algorithm)
        return encoded

    @staticmethod
    def decode_jwt(
        token: str | bytes,
        key: str = settings.auth_jwt.secret,
        algorithm: str = settings.auth_jwt.algorithm,
    ):
        """Декодирование JWT."""
        decoded = jwt.decode(jwt=token, key=key, algorithms=algorithm)
        return decoded


# def get_current_auth_token(
#     # credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
#     token: str = Depends(oauth_bearer),
# ) -> dict:
#     # token = credentials.credentials
#     try:
#         payload = utils_jwt.decode_jwt(token=token)
#     except InvalidTokenError as e:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail=f"Invalid token error: {e}",
#         )
#     return payload
#
#
# def get_current_auth_user(
#     payload: dict = Depends(get_current_auth_token),
# ) -> UserSchema:
#     username: str | None = payload.get("sub")
#
#     if user := users_db.get(username):
#         return user
#     raise HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Token invalid (user not found)",
#     )
