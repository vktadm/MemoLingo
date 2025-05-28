import pytest

from backend.app.services import CryptoService


@pytest.fixture
def crypto_service():
    return CryptoService()
