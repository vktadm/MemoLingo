from dataclasses import dataclass
from typing import Optional, List

from app.clients import ImageAPIClient
from app.exceptions import ConstraintViolationException
from app.repository import WordRepository
from app.schemas import WordSchema, CreateWordSchema, UpdateWordSchema


@dataclass
class WordService:

    repository: WordRepository
    image_client: ImageAPIClient

    async def create(self, new_data: CreateWordSchema) -> WordSchema:
        if await self.repository.get_word(wrd=new_data.wrd):
            raise ConstraintViolationException()
        img = await self.image_client.get_image(new_data.wrd)
        data = await self.repository.create_word(new_data, img)

        return WordSchema.model_validate(data)

    async def get_all(self) -> List[WordSchema]:
        data = await self.repository.get_words()

        return [WordSchema.model_validate(item) for item in data]

    async def get_by_id(self, id: int) -> WordSchema:
        data = await self.repository.get_word_by_id(id)

        return WordSchema.model_validate(data)

    async def update(self, id: int, update_data: UpdateWordSchema) -> WordSchema:
        data = await self.repository.update_word(update_data=update_data, word_id=id)

        return WordSchema.model_validate(data)

    async def delite(self, id: int) -> bool:
        return await self.repository.delete_word(id)
