from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.status import Status
from .schemas import UserWord
from . import crud

# from .dependencies import user_word_by_id
from core.models import db_helper

router = APIRouter(tags=["User Progress"])


@router.get("/{user_id}/", response_model=list[UserWord])
async def get_words(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_user_progress(
        session=session,
        user_id=user_id,
    )


@router.post("/{user_id}/", response_model=list[UserWord])
async def add_words_to_user(
    user_id: int,
    words_id: list[int],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    words = [
        UserWord(user_id=user_id, word_id=word_id, status=Status.NotStudy)
        for word_id in words_id
    ]

    return await crud.add_words_to_user_progress(session=session, words=words)


@router.patch("/{user_id}/", response_model=list[UserWord])
async def change_status_words_to_user(
    user_id: int,
    words_id: list[int],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    words = [
        UserWord(user_id=user_id, word_id=word_id, status=Status.NotStudy)
        for word_id in words_id
    ]

    return await crud.add_words_to_user_progress(session=session, words=words)
