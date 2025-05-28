from dataclasses import dataclass
from typing import List

from backend.src.app.clients import IconAPIClient
from backend.src.app.exceptions import ConstraintViolationException, NotFoundException
from backend.src.app.repository import CategoryRepository
from backend.src.app.schemas import (
    CategorySchema,
    CreateCategorySchema,
    UpdateCategorySchema,
)


@dataclass
class CategoryService:

    repository: CategoryRepository
    icon_client: IconAPIClient

    async def create(self, new_data: CreateCategorySchema) -> CategorySchema:
        if await self.repository.get_by_title(new_data.title):
            raise ConstraintViolationException()
        data = await self.repository.create(new_data)

        return CategorySchema.model_validate(data)

    async def get_all(self) -> List[CategorySchema]:
        data = await self.repository.get_all()
        if not data:
            raise NotFoundException()
        return [CategorySchema.model_validate(item) for item in data]

    async def get_by_id(self, id: int) -> CategorySchema:
        data = await self.repository.get_by_id(id)
        if not data:
            raise NotFoundException()

        return CategorySchema.model_validate(data)

    async def update(self, update_data: UpdateCategorySchema) -> CategorySchema:
        data = await self.repository.update(update_data)

        return CategorySchema.model_validate(data)

    async def delite(self, id: int):
        return await self.repository.delete(id)
