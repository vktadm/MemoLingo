import pytest
from dataclasses import dataclass
from faker import Factory

from app.schemas import GoogleUserDataSchema
from app.settings import GoogleSettings

faker = Factory.create()


@dataclass
class FakeGoogleClient:
    settings: GoogleSettings

    async def get_user_info(self, code: str) -> GoogleUserDataSchema:
        """Получает data из Google."""
        access_token = await self._get_user_access_token(code)
        return google_user_info_data()

    async def _get_user_access_token(self, code) -> str:
        """Получает токен доступа."""
        return f"fake_access_token {code}"


@pytest.fixture
def google_client():
    return FakeGoogleClient(settings=GoogleSettings())


def google_user_info_data() -> GoogleUserDataSchema:
    return GoogleUserDataSchema(
        username=faker.name(),
        google_access_token=faker.sha256(),
        email=faker.email(),
        name=faker.name(),
    )
