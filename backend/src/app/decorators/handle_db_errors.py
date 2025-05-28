from functools import wraps
from sqlalchemy.exc import SQLAlchemyError, IntegrityError, NoResultFound


from backend.src.app.exceptions import (
    NotFoundException,
    ContentConflictException,
    ConstraintViolationException,
    RepositoryException,
    DatabaseException,
)


def handle_db_errors(func):
    """Декоратор для обработки ошибок БД."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        operation = func.__name__
        try:
            return await func(*args, **kwargs)
        except NoResultFound:
            raise NotFoundException()

        except IntegrityError as e:
            print(f"{e} in {operation}.")
            if "unique constraint" in str(e).lower():
                raise ConstraintViolationException()
            raise ContentConflictException()

        except SQLAlchemyError as e:
            print(f"{e} in {operation}.")
            raise RepositoryException()

        except Exception as e:
            print(f"{e} in {operation}.")
            raise DatabaseException()

    return wrapper
