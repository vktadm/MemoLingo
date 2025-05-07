import httpx
from functools import wraps

from app.exceptions import ExternalServiceError, TimeoutError, RequestError


def handle_http_errors(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except httpx.HTTPStatusError as e:
            print(e)  # TODO: заменить на loggin
            raise ExternalServiceError

        except httpx.TimeoutException as e:
            print(e)
            raise TimeoutError

        except httpx.RequestError as e:
            print(e)
            raise RequestError

        except Exception as e:
            print(e)
            raise ExternalServiceError

    return wrapper
