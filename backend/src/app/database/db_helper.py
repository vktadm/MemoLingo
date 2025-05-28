from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from backend.src.app.settings import settings


class DatabaseHelper:
    def __init__(self, url, echo: bool = False):
        # Создание асинхронного движка базы данных
        # echo: Если True, выводит все SQL-запросы в консоль
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, expire_on_commit=False
        )

    def get_scoped_session(self):
        # Используется asyncio.current_task() для привязки к текущей задаче asyncio.
        session = async_scoped_session(
            session_factory=self.session_factory, scopefunc=current_task
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        # Через этот объект происходит работа с асинхронной БД
        async with self.session_factory() as session:
            yield session
            await session.close()


db_helper = DatabaseHelper(url=settings.db.get_url, echo=settings.db.echo)
