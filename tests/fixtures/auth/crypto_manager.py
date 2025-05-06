import pytest

from app.services import CryptoService


@pytest.fixture
def crypto_service():
    return CryptoService()
