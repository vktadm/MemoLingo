from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from api_v1.word.schemas import Word


router = APIRouter(tags=["Review"])


@router.get("/learn/{user_id}/", response_model=list[Word])
async def get_learn_words(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return None


@router.post("/learn/{user_id}/", response_model=list[Word])
async def create_learn_words(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return None


@router.get("/review/{user_id}/", response_model=list[Word])
async def get_review_words(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return None


@router.post("/review/{user_id}/", response_model=list[Word])
async def check_review_words(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return None
