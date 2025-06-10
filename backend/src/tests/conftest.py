import asyncio

import pytest

from .fixtures.clients import *
from .fixtures.models import *
from .fixtures.repository import *
from .fixtures.services import *
from .fixtures.infrastructure import *


# @pytest.fixture(scope="session")
# def event_loop():
#     loop = asyncio.get_event_loop()
#     yield loop
#     loop.close()
