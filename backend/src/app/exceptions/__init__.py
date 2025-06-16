from .auth import (
    UserIncorrectPasswordException,
    UserAlreadyExistsException,
    UserAlreadyConfirmException,
    UserForbiddenException,
    UserNotFoundException,
)
from .jwt import TokenException
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
    # Auth
    "UserAlreadyExistsException",
    "UserIncorrectPasswordException",
    "UserForbiddenException",
    "UserNotFoundException",
    # JWT
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
    "UserAlreadyConfirmException",
]
