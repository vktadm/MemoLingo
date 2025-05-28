import pytest

from backend.src.app.services import CryptoService


@pytest.fixture
def crypto_service():
    return CryptoService()
