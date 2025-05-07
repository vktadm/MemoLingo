from typing import Annotated, List, Optional
from fastapi import APIRouter, Depends, status

from app.dependencies import get_word_service

from app.schemas import WordSchema, CreateWordSchema, UpdateWordSchema
from app.services import WordService

router = APIRouter(prefix="/words", tags=["Words"])


@router.post(
    "/",
    response_model=WordSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_word(
    new_word: CreateWordSchema,
    service: Annotated[WordService, Depends(get_word_service)],
):
    word = await service.create_word(new_word=new_word)
    return word
