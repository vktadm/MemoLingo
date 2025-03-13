from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserWord
from . import crud
from core.models import db_helper


router = APIRouter(tags=["Revise Words"])


@router.get(
    "/random/",
    response_model=list[str],
)
async def random_words(
    word_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получает 3 случайных слова из БД."""
    # TODO Сейчас мы можем получить слова к несуществующему word_id
    words = await crud.get_random_words(
        session=session,
        word_id=word_id,
    )
    if not words:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=f"ERROR: No words",
        )
    return words


@router.get("/check/", response_model=bool)
async def check_word(
    wrd: str,
    user_choice: str,
):
    return wrd == user_choice


@router.get(
    "/words/{user_id}/",
    response_model=list[UserWord],
)
async def get_user_words(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    """Получает слова для повторения."""
    # TODO Вынести в dependencies
    user = await crud.user_by_id(user_id=user_id, session=session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ERROR: User {user_id} not found!",
        )

    words = await crud.get_user_words(
        session=session,
        user_id=user_id,
    )

    if not words:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=f"ERROR: No words for user_id: {user_id}",
        )

    return words
