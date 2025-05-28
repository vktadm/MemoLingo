import pytest

from backend.app.services import JWTService
from backend.app.settings import Settings


@pytest.fixture
def jwt_service():
    return JWTService(settings=Settings().auth_jwt)
