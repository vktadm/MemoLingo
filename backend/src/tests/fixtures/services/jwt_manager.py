import pytest

from backend.src.app.services import JWTService
from backend.src.app.settings import Settings


@pytest.fixture
def jwt_service():
    return JWTService(settings=Settings().auth_jwt)
