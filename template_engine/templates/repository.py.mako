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

    session: AsyncSession

    @handle_db_errors
    async def get_all(self) -> Optional[List[${name}]]:
        stmt = select(${name})
        result: Result = await self.session.execute(stmt)

        return list(result.scalars().all())

    @handle_db_errors
    async def get_by_id(self, id: int) -> Optional[${name}]:
        return await self.session.get(${name}, id)


    % for item in fields:
    % if item.unique:
    @handle_db_errors
    async def get_by_${item.name}(
        self,
        ${item.name}: str,
    ) -> Optional[${name}]:
        stmt = select(${name}).where(${name}.${item.name} == ${item.name})

        return await self.session.scalar(stmt)

    % endif
    % endfor
    @handle_db_errors
    async def create(self, new_data: Create${name}Schema) -> ${name}:
        data = ${name}(**new_data.model_dump())
        self.session.add(data)
        await self.session.commit()
        await self.session.flush()

        return data

    @handle_db_errors
    async def update(
        self,
        id: int,
        update_data: Update${name}Schema,
    ) -> ${name}:
        data = await self.get_by_id(id)
        if not data:
            raise NoResultFound()

        for key, value in update_data.model_dump().items():
            setattr(data, key, value)

        await self.session.commit()
        await self.session.refresh(data)

        return data

    @handle_db_errors
    async def delete(self, id: int) -> bool:
        data = await self.get_by_id(id)
        if not data:
            raise NoResultFound()

        await self.session.delete(data)
        await self.session.commit()

        return True
