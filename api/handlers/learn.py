from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import (
    IntegrityError,
    SQLAlchemyError,
    OperationalError,
)

from api.schemas import UserWord, CreateUserWord, Word
from api.services import learn as crud
from api.repository.user import UsersRepository
from database import db_helper


router = APIRouter(prefix="/learn", tags=["Learn Words"])


@router.get("/words/{user_id}/")
async def get_user_words(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
) -> list[Word]:
    """Получает новые слова для изучения."""
    repository = UsersRepository(session)
    user = await repository.get_user(user_id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: User {user_id} not found!",
        )

    words = await crud.get_new_user_words(
        session=session,
        user_id=user_id,
        quantity_words=3,
    )

    if not words:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=f"No words for user_id: {user_id}",
        )

    return words


@router.post(
    "/words/{user_id}/",
    response_model=list[UserWord],
    status_code=status.HTTP_201_CREATED,
)
async def add_user_words(
    user_id: int,
    new_words: list[CreateUserWord],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Создает прогресс по новым словам."""
    repository = UsersRepository(session)
    user = await repository.get_user(user_id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: User {user_id} not found!",
        )
    try:
        user_words = await crud.add_new_user_words(
            session=session,
            user_id=user_id,
            new_words=new_words,
        )
    except IntegrityError as e:
        # Обработка ошибок целостности (например, дубликаты)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"ERROR: Foreign key violations, duplicate entries.",
        )
    except OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"ERROR: Database connection error.",
        )
    except SQLAlchemyError as e:
        # Обработка других ошибок SQLAlchemy
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"ERROR: Couldn't insert data.",
        )

    return user_words
