from typing import Annotated, List
from fastapi import APIRouter, Depends, status

from backend.app.dependencies import get_category_service
from backend.app.schemas import (
    CategorySchema,
    CreateCategorySchema,
    UpdateCategorySchema,
)
from backend.app.services import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get(
    "/all",
    response_model=List[CategorySchema],
)
async def get_all(
    service: Annotated[CategoryService, Depends(get_category_service)],
):
    data = await service.get_all()
    return data


@router.get(
    "/{id}",
    response_model=CategorySchema,
)
async def get_by_id(
    id: int,
    service: Annotated[CategoryService, Depends(get_category_service)],
):
    data = await service.get_by_id(id)
    return data


@router.post(
    "/",
    response_model=CategorySchema,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    new_data: CreateCategorySchema,
    service: Annotated[CategoryService, Depends(get_category_service)],
):
    data = await service.create(new_data=new_data)
    return data


@router.patch(
    "/{id}",
    response_model=CategorySchema,
)
async def update(
    id: int,
    update_data: UpdateCategorySchema,
    service: Annotated[CategoryService, Depends(get_category_service)],
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
    service: Annotated[CategoryService, Depends(get_category_service)],
):
    await service.delite(id)
