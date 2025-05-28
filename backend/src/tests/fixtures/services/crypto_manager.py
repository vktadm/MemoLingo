import pytest

from backend_old.app.services import CryptoService


@pytest.fixture
def crypto_service():
    return CryptoService()
