import logging
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, NoResultFound


from backend.src.app.exceptions import (
    NotFoundException,
    ContentConflictException,
    ConstraintViolationException,
    RepositoryException,
    DatabaseException,
)

logger = logging.getLogger(__name__)


def handle_db_errors(func):
    """Декоратор для обработки ошибок БД."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        operation = func.__name__
        try:
            return await func(*args, **kwargs)

        except IntegrityError as e:
            logger.error(f"{e} in {operation}.")
            if "unique constraint" in str(e).lower():
                raise ConstraintViolationException()
            raise ContentConflictException()

        except SQLAlchemyError as e:
            logger.error(f"{e} in {operation}.")
            raise RepositoryException()

        except Exception as e:
            logger.error(f"{e} in {operation}.")
            raise DatabaseException()

    return wrapper
