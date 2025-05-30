import pytest

from typing import Optional
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.app.database import User
from backend.src.app.schemas import UserLoginSchema
from backend.src.app.services import GoogleAuthService, JWTService
from backend.src.tests.fixtures.models import (
    EXIST_GOOGLE_USER_EMAIL,
    EXIST_GOOGLE_USER_USERNAME,
)


@pytest.mark.asyncio(loop_scope="session")
async def test_google_auth_login_not_exist_user(
    google_auth_service: GoogleAuthService, session: AsyncSession
):
    code = "fake_code"

    users = (await session.execute(select(User))).scalars().all()
    user: Optional[UserLoginSchema] = await google_auth_service.auth_google(code)

    assert len(users) == 0
    assert user is not None

    login_user = (
        (await session.execute(select(User).where(User.id == user.id)))
        .scalars()
        .first()
    )

    stmt = delete(User).where(User.id == user.id)
    await session.execute(stmt)
    await session.commit()

    assert login_user is not None


@pytest.mark.asyncio(loop_scope="session")
async def test_google_auth_login_exist_user(
    google_auth_service: GoogleAuthService,
    jwt_service: JWTService,
    session: AsyncSession,
):
    code = "fake_code"

    query = insert(User).values(
        username=EXIST_GOOGLE_USER_USERNAME,
        email=EXIST_GOOGLE_USER_EMAIL,
        google_access_token=code,
    )
    await session.execute(query)
    await session.commit()

    user: Optional[UserLoginSchema] = await google_auth_service.auth_google(code)
    login_user: dict = jwt_service.decode_jwt(user.access_token)

    stmt = delete(User).where(User.id == user.id)
    await session.execute(stmt)
    await session.commit()

    assert login_user["username"] == EXIST_GOOGLE_USER_USERNAME
