import pytest

from backend.app.repository import UsersRepository
from backend.app.services import GoogleAuthService


@pytest.fixture
def mock_google_auth_service(
    fake_user_repository, google_client, jwt_service, fake_black_list
):
    return GoogleAuthService(
        user_repository=fake_user_repository,
        jwt_service=jwt_service,
        google_client=google_client,
        black_list=fake_black_list,
    )


@pytest.fixture
def google_auth_service(jwt_service, fake_black_list, session, google_client):
    return GoogleAuthService(
        user_repository=UsersRepository(session=session),
        google_client=google_client,
        jwt_service=jwt_service,
        black_list=fake_black_list,
    )
