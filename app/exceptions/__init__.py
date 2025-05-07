from app.exceptions.user import (
    UserNoCreate,
    UserNotFound,
    UserIncorrectPassword,
    UserAlreadyExists,
)
from app.exceptions.auth import TokenException, TokenExpired
from app.exceptions.db import (
    NotFound,
    ContentConflict,
    ConstraintViolationError,
    RepositoryError,
)
from app.exceptions.http import ExternalServiceError, TimeoutError, RequestError

__all__ = [
    # User
    "UserNotFound",
    "UserAlreadyExists",
    "UserIncorrectPassword",
    "UserNoCreate",
    # Auth
    "TokenExpired",
    "TokenException",
    # DB
    "NotFound",
    "ContentConflict",
    "ConstraintViolationError",
    "RepositoryError",
    # Clients
    "ExternalServiceError",
    "TimeoutError",
    "RequestError",
]
