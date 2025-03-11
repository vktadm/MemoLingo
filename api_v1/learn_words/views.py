from fastapi import APIRouter, Depends, status
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from ..word.schemas import Word as WordSchema
from ..user_progress.schemas import UserWord as UserWordSchema

from . import crud
from core.models import db_helper


router = APIRouter(tags=["Learn Words"])


@router.post(
    "/{user_id}/",
    response_model=list[UserWordSchema],
    status_code=status.HTTP_201_CREATED,
)
async def add_words_to_user(
    user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)
):
    # TODO: Проверка на существование пользователя -> raise
    # TODO: Сейчас возможно создавать UserProgres для несуществующего user
    words = await crud.get_new_user_words(
        session=session,
        user_id=user_id,
        quantity_words=5,
    )
    words = await crud.add_new_user_words(
        session=session,
        user_id=user_id,
        words_in=words,
    )
    # TODO: Если нет слов ?
    return words
