import pytest
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.app.database import User
from backend.src.app.exceptions import NotFoundException
from backend.src.app.schemas import UserLoginSchema
from backend.src.app.services import JWTService, AuthService, CryptoService


@pytest.mark.asyncio(loop_scope="session")
async def test_auth_login_not_exist_user(
    auth_service: AuthService, session: AsyncSession
):
    test_username = "test_username"
    test_password = "test_password"

    users = (await session.execute(select(User))).scalars().all()
    assert len(users) == 0

    with pytest.raises(NotFoundException):
        user: UserLoginSchema = await auth_service.login(test_username, test_password)


@pytest.mark.asyncio(loop_scope="session")
async def test_auths_login_exist_user(
    auth_service: AuthService,
    session: AsyncSession,
    jwt_service: JWTService,
    crypto_service: CryptoService,
):
    test_username = "test_username"
    test_password = "test_password"

    query = insert(User).values(
        username=test_username,
        password=crypto_service.hash_password(test_password),
    )
    await session.execute(query)
    await session.commit()

    login_user: UserLoginSchema = await auth_service.login(test_username, test_password)
    user_data = jwt_service.decode_jwt(login_user.access_token)

    stmt = delete(User).where(User.id == login_user.id)
    await session.execute(stmt)
    await session.commit()

    assert user_data["username"] == test_username
