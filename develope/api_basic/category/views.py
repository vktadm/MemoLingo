from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.category import (
    Category,
    CategoryCreate,
    CategoryUpdate,
    CategoryUpdatePartial,
)
from . import crud
from .dependencies import category_by_id
from core.models import db_helper

router = APIRouter(tags=["Categories"])


@router.get("/", response_model=list[Category])
async def get_categories(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_categories(session=session)


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_in: CategoryCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_category(session=session, category_in=category_in)


@router.get("/{category_id}/", response_model=Category)
async def get_category(category: Category = Depends(category_by_id)):
    return category


@router.patch("/{category_id}/")
async def update_category(
    category_update: CategoryUpdate | CategoryUpdatePartial,
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_category(
        session=session,
        category=category,
        category_update=category_update,
        partial=True,
    )


@router.delete("/{category_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await crud.delete_category(session=session, category=category)
