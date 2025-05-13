from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import (
    IntegrityError,
    SQLAlchemyError,
    OperationalError,
)

from backend.app.schemas import UserWordSchema, CreateUserWordSchema, WordSchema
from backend.app.services import learn as crud
from backend.app.dependencies import get_request_user_id
from backend.app.database import db_helper

router = APIRouter(prefix="/learn", tags=["Learn Words"])


@router.get(
    "/words/",
    response_model=list[WordSchema],
)
async def get_user_words(
    user_id: int = Depends(get_request_user_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получает новые слова для изучения."""
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
    "/words/",
    response_model=list[UserWordSchema],
    status_code=status.HTTP_201_CREATED,
)
async def add_user_words(
    new_words: list[CreateUserWordSchema],
    user_id: int = Depends(get_request_user_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Создает прогресс по новым словам."""
    try:
        user_words = await crud.add_new_user_words(
            user_id=user_id,
            session=session,
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
