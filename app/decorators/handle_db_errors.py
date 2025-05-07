from functools import wraps
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, NoResultFound, DatabaseError

from app.exceptions import (
    NotFound,
    ContentConflict,
    ConstraintViolationError,
    RepositoryError,
)


async def handle_db_errors(func):
    """Декоратор для обработки ошибок БД."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        operation = func.__name__
        try:
            return await func(*args, **kwargs)
        except NotFound:
            raise
        except IntegrityError as e:
            print(f"{e} in {operation}.")
            if "unique constraint" in str(e).lower():
                raise ConstraintViolationError
            raise ContentConflict
        except SQLAlchemyError as e:
            print(f"{e} in {operation}.")
            raise RepositoryError
        except Exception as e:
            print(f"{e} in {operation}.")
            raise DatabaseError

    return wrapper
