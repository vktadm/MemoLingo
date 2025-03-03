from pathlib import Path
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Category
from . import crud


async def category_by_id(
    category_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Category:
    category = await crud.get_category(session=session, category_id=category_id)
    if category:
        return category
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Category {category_id} not found!",
    )
