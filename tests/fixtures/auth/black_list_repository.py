import pytest
from dataclasses import dataclass


@dataclass
class FakeTokenBlackListRepository:
    pass


@pytest.fixture
def black_list():
    return FakeTokenBlackListRepository()
