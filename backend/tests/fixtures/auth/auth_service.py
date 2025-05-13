import pytest

from app.services import AuthService


@pytest.fixture
def auth_service(
    user_repository, google_client, jwt_service, crypto_service, black_list
):
    return AuthService(
        user_repository=user_repository,
        jwt_service=jwt_service,
        crypto_service=crypto_service,
        black_list=black_list,
    )
