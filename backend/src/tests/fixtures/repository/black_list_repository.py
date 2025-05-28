import pytest
from dataclasses import dataclass


@dataclass
class FakeTokenBlackListRepository:
    async def add_token(self, token: str):
        pass

    async def block_token(self, token: str):
        pass

    async def token_is_expired(self, token: str) -> bool:
        return True


@pytest.fixture
def fake_black_list():
    return FakeTokenBlackListRepository()
