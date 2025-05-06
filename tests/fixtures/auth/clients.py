import pytest
from dataclasses import dataclass

from app.settings import GoogleSettings


@dataclass
class FakeGoogleClient:
    settings: GoogleSettings

    async def get_user_info(self, code: str) -> dict:
        """Получает data из Google."""
        access_token = await self._get_user_access_token(code)
        return {"fake_access_token": access_token}

    async def _get_user_access_token(self, code) -> str:
        """Получает токен доступа."""
        return f"fake_access_token {code}"


@pytest.fixture
def google_client():
    return FakeGoogleClient(settings=GoogleSettings())
