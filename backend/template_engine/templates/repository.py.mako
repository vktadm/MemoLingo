from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from app.database import ${name}
from app.decorators import handle_db_errors
from app.schemas import Create${name}Schema, Update${name}Schema


@dataclass
class ${name}Repository:
    """
    Класс-репозиторий для работы с моделью в базе данных.
    Реализует CRUD (Create, Read, Update, Delete) операции.
    Использует асинхронный SQLAlchemy для работы с БД.
    """

    session: AsyncSession # Асинхронная сессия для работы с БД

    @handle_db_errors
    async def get_all(self) -> Optional[List[${name}]]:
        """Получает все объекты из базы данных."""
        stmt = select(${name})
        result: Result = await self.session.execute(stmt)

        return list(result.scalars().all())

    @handle_db_errors
    async def get_by_id(self, id: int) -> Optional[${name}]:
        """Получает обхъект по идентификатору."""
        return await self.session.get(${name}, id)


    % for item in fields:
    % if item.unique:
    @handle_db_errors
    async def get_by_${item.name}(
        self,
        ${item.name}: str,
    ) -> Optional[${name}]:
        """Получает объект по уникальному значению."""
        stmt = select(${name}).where(${name}.${item.name} == ${item.name})

        return await self.session.scalar(stmt)

    % endif
    % endfor
    @handle_db_errors
    async def create(self, new_data: Create${name}Schema) -> ${name}:
        """Создает новый объект в базе данных."""
        data = ${name}(**new_data.model_dump())
        self.session.add(data)
        await self.session.commit()
        await self.session.flush()

        return data

    @handle_db_errors
    async def update(
        self,
        update_data: Update${name}Schema,
    ) -> ${name}:
        """Обновляет существующий объект."""
        data = await self.get_by_id(update_data.id)
        if not data:
            raise NoResultFound()

        for key, value in update_data.model_dump().items():
            setattr(data, key, value)

        await self.session.commit()
        await self.session.refresh(data)

        return data

    @handle_db_errors
    async def delete(self, id: int):
        """Удаляет объект из базы данных."""
        data = await self.get_by_id(id)
        if not data:
            raise NoResultFound()

        await self.session.delete(data)
        await self.session.commit()
