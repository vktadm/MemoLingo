from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from core.config import settings


class DatabaseHelper:
    def __init__(self, url, echo: bool = False):
        # Создание асинхронного движка базы данных,
        # который позволяет выполнять операции с базой данных в асинхронном режиме

        # echo: Если True, выводит все SQL-запросы в консоль
        self.engine = create_async_engine(url=url, echo=echo)  # TODO: отладка

        # Создавает асинхронные сессии для взаимодействия с базой данных
        # bind: Привязка к движку базы данных, созданному с помощью create_async_engine

        # autoflush: Если True, сессия будет автоматически сбрасывать изменения в базу данных

        # expire_on_commit: Если True, объекты в сессии будут считаться устаревшими
        # и потребуют повторного запроса к базе данных для обновления.

        # autocommit=False: транзакции не будут автоматически подтверждаться.
        # нужно будет вызывать await session.commit() для подтверждения изменений.
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, expire_on_commit=False
        )

    def get_scoped_session(self):
        # позволяет создавать асинхронные сессии, привязанные к определенному контексту,
        # например, к текущей задаче asyncio или запросу в FastAPI

        # возвращает уникальный идентификатор для каждого контекста
        # sessionmaker: Фабрика асинхронных сессий, созданная с помощью async_sessionmaker.
        #
        # scopefunc: Функция, которая возвращает уникальный идентификатор для каждого контекста.
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


db_helper = DatabaseHelper(url=settings.db.url, echo=settings.db.echo)
