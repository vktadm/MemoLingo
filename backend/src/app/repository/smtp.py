import logging
from dataclasses import dataclass
from datetime import timedelta

from redis.asyncio import Redis

from backend.src.app.exceptions import SMTPTokenException


logger = logging.getLogger(__name__)


@dataclass
class SMTPRepository:
    session: Redis
    expiration_time: timedelta = timedelta(hours=24)
    resend_time: timedelta = timedelta(minutes=1)

    async def add_token(self, token: str, email: str):
        """Сохраняем новый токен (24 часа)."""
        seconds = int(self.expiration_time.total_seconds())
        token_key = f"email_verify:{token}"

        await self.session.setex(
            name=token_key,
            time=seconds,
            value=email,
        )
        await self.session.sadd(f"email_tokens:{email}", token_key)

    async def set_email_cooldown(self, email: str):
        """Устанавливаем лимит на повторную отправку."""
        seconds = int(self.resend_time.total_seconds())
        await self.session.setex(f"email_cooldown:{email}", seconds, "1")

    async def verify_token(self, token: str):
        """Проверяет токен и возвращает email если он валиден."""
        token_key = f"email_verify:{token}"
        email = await self.session.get(token_key)
        if not email:
            logger.info(f"Attempt to confirm invalid token: {token}")
            raise SMTPTokenException()

        return email.decode("utf-8")

    async def verify_cooldown(self, email: str):
        email_key = f"email_cooldown:{email}"
        return await self.session.get(email_key)

    async def revoke_existing_tokens(self, email: str):
        """Удаляет все активные токены для указанного email."""
        email_tokens_key = f"email_tokens:{email}"

        tokens = await self.session.smembers(email_tokens_key)
        if tokens:
            await self.session.delete(*tokens)
            await self.session.delete(email_tokens_key)
