import logging
from functools import wraps
from jwt import ExpiredSignatureError, PyJWTError

from backend.src.app.exceptions import TokenException, TokenExpiredException

logger = logging.getLogger(__name__)


def handle_jwt_manager_errors(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        operation = func.__name__
        try:
            return func(*args, **kwargs)
        except ExpiredSignatureError as e:
            logger.error(f"{e} in {operation}")
            raise TokenExpiredException()
        except PyJWTError as e:
            logger.error(f"{e} in {operation}")
            raise TokenException()

    return wrapper
