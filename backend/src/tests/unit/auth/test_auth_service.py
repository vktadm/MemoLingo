import pytest
from datetime import datetime as dt, timezone, timedelta

from backend_old.app.schemas import UserSchema
from backend_old.app.services import AuthService, JWTService

from backend_old.app.settings import Settings

pytestmark = pytest.mark.asyncio


def test_create_access_token__success(
    mock_auth_service: AuthService,
    jwt_service: JWTService,
    settings: Settings,
):
    user_id = 1
    username = "username"
    user = UserSchema(id=user_id, username=username)

    access_token = mock_auth_service._create_access_token(user)
    decode_access_token = jwt_service.decode_jwt(access_token)
    decoded_user_id = decode_access_token["id"]
    decoded_username = decode_access_token["username"]
    decoded_expire = dt.fromtimestamp(decode_access_token["exp"], tz=timezone.utc)

    assert (decoded_expire - dt.now(tz=timezone.utc)) > timedelta(
        minutes=settings.auth_jwt.access_token_expire_minutes - 1
    )
    assert decoded_user_id == user_id
    assert decoded_username == username
