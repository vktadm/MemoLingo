import pytest
from datetime import datetime as dt, timezone, timedelta

from app.services import JWTService

pytestmark = pytest.mark.asyncio


def test_encode_decode_jwt__success(
    jwt_service: JWTService,
):
    payload = {
        "data": "some_data",
    }

    token = jwt_service.encode_jwt(payload)
    decode_token = jwt_service.decode_jwt(token)
    decoded_expire = dt.fromtimestamp(decode_token["exp"], tz=timezone.utc)

    assert (decoded_expire - dt.now(tz=timezone.utc)) > timedelta(
        minutes=jwt_service.settings.access_token_expire_minutes - 1
    )
    assert payload["data"] == decode_token["data"]
