import logging

import httpx
from functools import wraps

from backend.src.app.exceptions import (
    ExternalServiceException,
    TimeoutException,
    RequestException,
)

logger = logging.getLogger(__name__)


def handle_client_errors(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):
        operation = func.__name__
        try:
            return await func(*args, **kwargs)

        except httpx.HTTPStatusError as e:
            logger.error(f"{e} in {operation}")
            raise ExternalServiceException()

        except httpx.TimeoutException as e:
            logger.error(f"{e} in {operation}")
            raise TimeoutException()

        except httpx.RequestError as e:
            logger.error(f"{e} in {operation}")
            raise RequestException()

        except Exception as e:
            logger.error(f"{e} in {operation}")
            raise ExternalServiceException()

    return wrapper
