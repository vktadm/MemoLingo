import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from backend.src.app.settings import settings as app_settings, Settings
from .settings import fake_settings
from backend.src.app.database import Base


@pytest.fixture
def settings() -> Settings:
    return app_settings


engine = create_async_engine(url=fake_settings.db.get_url, echo=True)
session_factory = async_sessionmaker(
    bind=engine, autoflush=False, expire_on_commit=False
)


@pytest.fixture(scope="session", autouse=True)
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
async def session() -> AsyncSession:
    async with session_factory() as session:
        yield session
        await session.close()
