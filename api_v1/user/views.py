from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import User, CreateUser
from .dependencies import user_by_id
from . import crud
from core.models import db_helper


router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[User])
async def get_users(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_users(session=session)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    word_in: CreateUser,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_user(session=session, user_in=word_in)


@router.get("/{user_id}/", response_model=User)
async def get_word(word: User = Depends(user_by_id)):
    return word
