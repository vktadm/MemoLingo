from dataclasses import dataclass
from typing import Optional

from app.clients.image import ImageAPIClient
from app.exceptions import ConstraintViolationException
from app.repository import WordRepository
from app.schemas import WordSchema, CreateWordSchema, UpdateWordSchema


@dataclass
class WordService:

    word_repository: WordRepository  # Доступ к данным пользователей в БД
    image_client: ImageAPIClient

    async def create_word(self, new_word: CreateWordSchema) -> WordSchema:
        if await self.word_repository.get_word(wrd=new_word.wrd):
            raise ConstraintViolationException()
        img = await self.image_client.get_image(new_word.wrd)
        word = await self.word_repository.create_word(new_word, img)
        # TODO: Ошибки при преобразовании Word -> WordSchema

        return WordSchema.model_validate(word)
