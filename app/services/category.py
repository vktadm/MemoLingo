from dataclasses import dataclass
from typing import Optional

from app.clients import IconAPIClient
from app.exceptions import ConstraintViolationException
from app.repository import CategoryRepository
from app.schemas import CategorySchema, CreateCategorySchema, UpdateCategorySchema


@dataclass
class CategoryService:

    category_repository: CategoryRepository  # Доступ к данным категорий в БД
    icon_client: IconAPIClient

    async def create_category(
        self, new_category: CreateCategorySchema
    ) -> CategorySchema:
        if await self.category_repository.get_category(title=new_category.title):
            raise ConstraintViolationException()
        img = await self.icon_client.get_image(new_category.title)
        category = await self.category_repository.create_category(new_category, img)
        # TODO: Ошибки при преобразовании Category -> CategorySchema

        return CategorySchema.model_validate(category)
