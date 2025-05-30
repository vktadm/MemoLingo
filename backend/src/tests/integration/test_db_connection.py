import pytest
from sqlalchemy import Result, text
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio(loop_scope="session")
async def test_db_connection__success(session: AsyncSession):
    assert type(session) == AsyncSession
    result: Result = await session.execute(text("SELECT 1"))
    assert result.scalar() == 1
    await session.close()
