import pytest

from app.services import GoogleAuthService


@pytest.fixture
def google_auth_service(
    user_repository, google_client, jwt_service, crypto_service, black_list
):
    return GoogleAuthService(
        user_repository=user_repository,
        jwt_service=jwt_service,
        google_client=google_client,
        black_list=black_list,
    )
