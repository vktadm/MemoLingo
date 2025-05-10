from typing import Annotated, List
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
    new_data: CreateWordSchema,
    service: Annotated[WordService, Depends(get_word_service)],
):
    data = await service.create(new_data=new_data)
    return data


@router.get(
    "/{id}",
    response_model=WordSchema,
)
async def get_by_id(
    id: int,
    service: Annotated[WordService, Depends(get_word_service)],
):
    data = await service.get_by_id(id)
    return data


@router.get(
    "/all",
    response_model=List[WordSchema],
)
async def get_all(
    service: Annotated[WordService, Depends(get_word_service)],
):
    data = await service.get_all()
    return data


@router.patch(
    "/{id}",
    response_model=WordSchema,
)
async def update_word(
    id: int,
    update_data: UpdateWordSchema,
    service: Annotated[WordService, Depends(get_word_service)],
):
    data = await service.update(id=id, update_data=update_data)
    return data


@router.delete(
    "/{id}",
    response_model=WordSchema,
)
async def delete(
    id: int,
    service: Annotated[WordService, Depends(get_word_service)],
):
    return await service.delite(id)
