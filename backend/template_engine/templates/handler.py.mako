from typing import Annotated, List
from fastapi import APIRouter, Depends, status

from app.dependencies import get_${name.lower()}_service
from app.schemas import ${name}Schema, Create${name}Schema, Update${name}Schema
from app.services import ${name}Service

router = APIRouter(prefix="/[your_prefix]", tags=["[your_tag]"])


@router.get(
    "/all",
    response_model=List[${name}Schema],
)
async def get_all(
    service: Annotated[${name}Service, Depends(get_${name.lower()}_service)],
):
    data = await service.get_all()
    return data


@router.get(
    "/{id}",
    response_model=${name}Schema,
)
async def get_by_id(
    id: int,
    service: Annotated[${name}Service, Depends(get_${name.lower()}_service)],
):
    data = await service.get_by_id(id)
    return data


@router.post(
    "/",
    response_model=${name}Schema,
    status_code=status.HTTP_201_CREATED,
)
async def create(
    new_data: Create${name}Schema,
    service: Annotated[${name}Service, Depends(get_${name.lower()}_service)],
):
    data = await service.create(new_data=new_data)
    return data


@router.patch(
    "/{id}",
    response_model=${name}Schema,
)
async def update(
    id: int,
    update_data: Update${name}Schema,
    service: Annotated[${name}Service, Depends(get_${name.lower()}_service)],
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
    service: Annotated[${name}Service, Depends(get_${name.lower()}_service)],
):
    await service.delite(id)
