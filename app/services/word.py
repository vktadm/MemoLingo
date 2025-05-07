from dataclasses import dataclass
from typing import Optional

from app.clients.image import ImageAPIClient
from app.exceptions import ContentConflict
from app.exceptions import NotFound
from app.repository import WordRepository
from app.schemas import WordSchema, CreateWordSchema, UpdateWordSchema


@dataclass
class WordService:

    word_repository: WordRepository  # Доступ к данным пользователей в БД
    image_client: ImageAPIClient

    async def create_word(self, new_word: CreateWordSchema) -> WordSchema:
        if await self.word_repository.get_word(wrd=new_word.wrd):
            raise ContentConflict

        new_word.img = await self.image_client.get_image(new_word.wrd)
        word = await self.word_repository.create_word(new_word)

        return UserSchema(id=user.id, username=user.username, email=user.email)

    async def get_users(self) -> list[UserSchema]:
        """Получает список всех пользователей."""
        data = await self.user_repository.get_users()
        users = [
            UserSchema(
                id=user.id,
                username=user.username,
                email=user.email,
                name=user.name,
            )
            for user in data
        ]
        if not users:
            raise NotFound
        return users

    async def get_user_by_id(self, user_id: int) -> UserSchema:
        """Получает пользователя по его идентификатору."""
        data = await self.user_repository.get_user_by_id(user_id=user_id)
        user = UserSchema(
            id=data.id,
            username=data.username,
            email=data.email,
            name=data.name,
        )
        if not user:
            raise NotFound
        return user
