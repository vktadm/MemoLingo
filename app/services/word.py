from dataclasses import dataclass
from typing import Optional, List

from app.clients import ImageAPIClient
from app.exceptions import ConstraintViolationException, NotFoundException
from app.repository import WordRepository
from app.schemas import WordSchema, CreateWordSchema, UpdateWordSchema


@dataclass
class WordService:

    repository: WordRepository
    image_client: ImageAPIClient

    async def create(self, new_data: CreateWordSchema) -> WordSchema:
        if await self.repository.get_by_wrd(wrd=new_data.wrd):
            raise ConstraintViolationException()
        new_data.img = await self.image_client.get_image(new_data.wrd)
        data = await self.repository.create(new_data)

        return WordSchema.model_validate(data)

    async def get_all(self) -> List[WordSchema]:
        data = await self.repository.get_all()

        return [WordSchema.model_validate(item) for item in data]

    async def get_by_id(self, id: int) -> WordSchema:
        data = await self.repository.get_by_id(id)
        if not data:
            raise NotFoundException()

        return WordSchema.model_validate(data)

    async def update(self, update_data: UpdateWordSchema) -> WordSchema:
        data = await self.repository.update(update_data=update_data)

        return WordSchema.model_validate(data)

    async def delite(self, id: int):
        await self.repository.delete(id)
