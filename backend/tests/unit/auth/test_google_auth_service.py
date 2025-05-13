from datetime import timezone, timedelta, datetime as dt

import pytest

from app.schemas import UserSchema, UserLoginSchema
from app.services import GoogleAuthService, JWTService
from app.settings import Settings

pytestmark = pytest.mark.asyncio


def test_google_redirect_url__success(
    google_auth_service: GoogleAuthService,
    settings: Settings,
):
    settings_google_redirect_url = google_auth_service.get_google_redirect_url

    auth_service_google_redirect_url = google_auth_service.get_google_redirect_url

    assert settings_google_redirect_url == auth_service_google_redirect_url


def test_google_redirect_url__fail(
    google_auth_service: GoogleAuthService,
):
    settings_google_redirect_url = "https://fake_google_redirect_url.com"

    auth_service_google_redirect_url = google_auth_service.get_google_redirect_url

    assert settings_google_redirect_url != auth_service_google_redirect_url


def test_create_access_token__success(
    google_auth_service: GoogleAuthService,
    jwt_service: JWTService,
    settings: Settings,
):
    user_id = 2
    username = "google_username"
    user = UserSchema(id=user_id, username=username)

    access_token = google_auth_service._create_access_token(user)
    decode_access_token = jwt_service.decode_jwt(access_token)
    decoded_user_id = decode_access_token["id"]
    decoded_username = decode_access_token["username"]
    decoded_expire = dt.fromtimestamp(decode_access_token["exp"], tz=timezone.utc)

    assert (decoded_expire - dt.now(tz=timezone.utc)) > timedelta(
        minutes=settings.auth_jwt.access_token_expire_minutes - 1
    )
    assert decoded_user_id == user_id
    assert decoded_username == username


async def test_auth_google__success(
    google_auth_service: GoogleAuthService,
):
    code = "fake_code"

    user = await google_auth_service.auth_google(code=code)
    access_token = user.access_token
    decoded_user = google_auth_service.jwt_service.decode_jwt(access_token)

    assert isinstance(user, UserLoginSchema)
    assert user.id == decoded_user["id"]


if __name__ == "__main__":
    pytest.main()
