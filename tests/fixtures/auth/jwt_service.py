import pytest
from dataclasses import dataclass

from app.services import JWTService
from app.settings import Settings


@pytest.fixture
def jwt_service():
    return JWTService(settings=Settings().auth_jwt)
