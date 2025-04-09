from pathlib import Path
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper, Word
from . import crud


async def word_by_id(
    word_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Word:
    word = await crud.get_word(session=session, word_id=word_id)
    if word:
        return word
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Word {word_id} not found!",
    )
