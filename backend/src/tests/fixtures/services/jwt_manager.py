import pytest

from backend_old.app.services import JWTService
from backend_old.app.settings import Settings


@pytest.fixture
def jwt_service():
    return JWTService(settings=Settings().auth_jwt)
