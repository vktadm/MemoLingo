import httpx
import logging
from functools import wraps

from app.exceptions import ExternalServiceException, TimeoutException, RequestException


def handle_client_errors(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except httpx.HTTPStatusError as e:
            print(e)  # TODO: заменить на loggin
            raise ExternalServiceException()

        except httpx.TimeoutException as e:
            print(e)
            raise TimeoutException()

        except httpx.RequestError as e:
            print(e)
            raise RequestException()

        except Exception as e:
            print(e)
            raise ExternalServiceException()

    return wrapper
