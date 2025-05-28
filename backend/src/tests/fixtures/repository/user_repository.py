from typing import Optional

import pytest
from dataclasses import dataclass

from backend.src.tests.fixtures.models import UserFactory


@dataclass
class FakeUserRepository:
    async def get_user_by_email(self, email: str) -> None:
        return None

    async def create_google_user(
        self,
        username: str,
        google_access_token: str,
        name: Optional[str] = None,
        email: Optional[str] = None,
        is_active: bool = True,
    ) -> UserFactory:
        return UserFactory()


@pytest.fixture
def fake_user_repository():
    return FakeUserRepository()
