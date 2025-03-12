from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Word, WordCreate, WordUpdate
from . import crud
from .dependencies import word_by_id
from core.models import db_helper

router = APIRouter(tags=["Words"])


@router.get("/", response_model=list[Word])
async def get_words(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_words(session=session)


@router.post("/", response_model=Word, status_code=status.HTTP_201_CREATED)
async def create_word(
    word_in: WordCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_word(session=session, word_in=word_in)


@router.get("/{word_id}/", response_model=Word)
async def get_word(word: Word = Depends(word_by_id)):
    return word


@router.patch("/{word_id}/")
async def update_word(
    word_update: WordUpdate,
    word: Word = Depends(word_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_word(
        session=session, word=word, word_update=word_update, partial=True
    )


@router.delete("/{word_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_word(
    word: Word = Depends(word_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await crud.delete_word(session=session, word=word)
