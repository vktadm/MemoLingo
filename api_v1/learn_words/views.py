from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import NewUserWord, UserWord
from . import crud
from core.models import db_helper


router = APIRouter(tags=["Learn Words"])


@router.get(
    "/words/{user_id}/",
    response_model=list[NewUserWord],
)
async def get_user_words(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Получает новые слова для изучения."""

    user = await crud.user_by_id(user_id=user_id, session=session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: User {user_id} not found!",
        )

    new_words = await crud.get_new_user_words(
        session=session,
        user_id=user_id,
        quantity_words=5,
    )

    if not new_words:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=f"No words for user_id: {user_id}",
        )

    return new_words


@router.post(
    "/words/{user_id}/",
    response_model=list[UserWord],
    status_code=status.HTTP_201_CREATED,
)
async def add_user_words(
    user_id: int,
    new_words: list[NewUserWord],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Создает прогресс по новым словам."""

    user_words = await crud.add_new_user_words(
        session=session,
        user_id=user_id,
        new_words=new_words,
    )

    return user_words
