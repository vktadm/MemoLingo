import pytest

from backend.src.app.repository import UsersRepository
from backend.src.app.services import AuthService


@pytest.fixture
def mock_auth_service(
    fake_user_repository, jwt_service, crypto_service, fake_black_list
):
    return AuthService(
        user_repository=fake_user_repository,
        jwt_service=jwt_service,
        crypto_service=crypto_service,
        black_list=fake_black_list,
    )


@pytest.fixture
def auth_service(jwt_service, crypto_service, fake_black_list, session):
    return AuthService(
        user_repository=UsersRepository(session=session),
        jwt_service=jwt_service,
        crypto_service=crypto_service,
        black_list=fake_black_list,
    )
