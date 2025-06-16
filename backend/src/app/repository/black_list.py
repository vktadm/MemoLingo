from dataclasses import dataclass
from redis.asyncio import Redis

from backend.src.app.settings import Settings


class TokenStatus:
    ACTIVE = "active"
    REVOKED = "revoked"


@dataclass
class TokenBlackListRepository:
    session: Redis
    settings: Settings

    async def add_token(self, token: str):
        expiration = self.settings.auth_jwt.access_token_expire_minutes * 60
        await self.session.set(token, TokenStatus.ACTIVE, ex=expiration)

    async def block_token(self, token: str):
        await self.session.delete(token)

    async def token_is_expired(self, token: str) -> bool:
        exists = await self.session.exists(token)
        return not exists
