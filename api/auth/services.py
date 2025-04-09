from typing import Annotated

from fastapi import Form, HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import User, db_helper
from api.auth import crypto


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    return await session.scalar(stmt)


async def validate_user(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> User:
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Неверное имя пользователя или пароль",
    )
    user = await get_user_by_username(session, username)
    if not user:
        raise exception
    if crypto.validate_password(password, user.password):
        return user
    raise exception


async def create_user(
    username: str = Form(),
    password: str = Form(),
    # email: EmailStr = Form(default=None),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> User:
    # TODO: Обработка ошибок
    user = User(username=username, password=crypto.hash_password(password))
    session.add(user)
    await session.commit()
    return user


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
