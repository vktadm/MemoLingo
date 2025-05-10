from dataclasses import dataclass
from typing import Optional, List

from app.exceptions import ConstraintViolationException
from app.repository import ${name}Repository
from app.schemas import ${name}Schema, Create${name}Schema, Update${name}Schema


@dataclass
class ${name}Service:

    repository: ${name}Repository

    async def create(self, new_data: Create${name}Schema) -> ${name}Schema:
        if await self.repository.get_all(new_data.change):
            raise ConstraintViolationException()
        data = await self.repository.create(new_data)

        return ${name}Schema.model_validate(data)

    async def get_all(self) -> List[${name}Schema]:
        data = await self.repository.get_words()

        return [${name}Schema.model_validate(item) for item in data]

    async def get_by_id(self, id: int) -> ${name}Schema:
        data = await self.repository.get_by_id(id)

        return ${name}Schema.model_validate(data)

    async def update(self, update_data: Update${name}Schema) -> ${name}Schema:
        data = await self.repository.update(update_data)

        return ${name}Schema.model_validate(data)

    async def delite(self, id: int) -> bool:
        return await self.repository.delete(id)
