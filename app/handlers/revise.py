from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_request_user_id
from app.schemas import WordSchema
from app.services import revise as crud
from app.database import db_helper

router = APIRouter(prefix="/revise", tags=["Revise Words"])


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


@router.get("/words", response_model=list[WordSchema])
async def get_user_words(
    user_id: int = Depends(get_request_user_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    """Получает слова для повторения."""
    # TODO Вынести в dependencies
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
