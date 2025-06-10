from .auth import (
    TokenException,
    TokenExpiredException,
    UserIncorrectPasswordException,
    UserAlreadyExistsException,
    UserAlreadyConfirmException,
)
from .db import (
    NotFoundException,
    ContentConflictException,
    ConstraintViolationException,
    RepositoryException,
    DatabaseException,
)
from .client import (
    ExternalServiceException,
    TimeoutException,
    RequestException,
)


from .smtp import SMTPTokenException, SMTPException, SMTPCooldownException

__all__ = [
    # User
    "UserAlreadyExistsException",
    "UserIncorrectPasswordException",
    # Auth
    "TokenExpiredException",
    "TokenException",
    # DB
    "NotFoundException",
    "ContentConflictException",
    "ConstraintViolationException",
    "RepositoryException",
    "DatabaseException",
    # Clients
    "ExternalServiceException",
    "TimeoutException",
    "RequestException",
    # SMTP
    "SMTPException",
    "SMTPTokenException",
    "SMTPCooldownException",
]
