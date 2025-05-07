import logging
from functools import wraps
from jwt import ExpiredSignatureError, PyJWTError

from app.exceptions import TokenException, TokenExpiredException


def handle_jwt_manager_errors(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        operation = func.__name__
        try:
            return func(*args, **kwargs)
        except ExpiredSignatureError as e:
            print(f"{e} in {operation}.")
            raise TokenExpiredException()
        except PyJWTError as e:
            print(f"{e} in {operation}.")
            raise TokenException()

    return wrapper
