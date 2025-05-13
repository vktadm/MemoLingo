from typing import Annotated, List
from fastapi import APIRouter, Depends, status

from backend.app.dependencies import get_word_service
from backend.app.schemas import WordSchema, CreateWordSchema, UpdateWordSchema
from backend.app.services import WordService

router = APIRouter(prefix="/words", tags=["Words"])


@router.get(
    "/all",
    response_model=List[WordSchema],
)
async def get_all(
    service: Annotated[WordService, Depends(get_word_service)],
):
    data = await service.get_all()
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


@router.post(
    "/",
    response_model=WordSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    new_data: CreateWordSchema,
    service: Annotated[WordService, Depends(get_word_service)],
):
    data = await service.create(new_data=new_data)
    return data


@router.patch(
    "/{id}",
    response_model=WordSchema,
)
async def update(
    id: int,
    update_data: UpdateWordSchema,
    service: Annotated[WordService, Depends(get_word_service)],
):
    update_data.id = id
    data = await service.update(update_data=update_data)
    return data


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    id: int,
    service: Annotated[WordService, Depends(get_word_service)],
):
    await service.delite(id)
