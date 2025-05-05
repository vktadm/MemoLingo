import pytest
from dataclasses import dataclass

from app.services import CryptoService


@pytest.fixture
def crypto_service():
    return CryptoService()
