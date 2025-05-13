from dataclasses import dataclass
from redis.asyncio import Redis

from backend.app.settings import Settings


@dataclass
class TokenBlackListRepository:
    session: Redis
    settings: Settings

    async def add_token(self, token: str):
        expiration = self.settings.auth_jwt.access_token_expire_minutes * 60
        await self.session.set(token, 0, ex=expiration)

    async def block_token(self, token: str):
        ttl = await self.session.ttl(token)
        if ttl != -2:
            await self.session.setex(token, ttl, 1)

    async def token_is_expired(self, token: str) -> bool:
        is_expired = await self.session.get(token)
        if not is_expired:
            return True
        return bool(int(is_expired.decode("utf-8")))
