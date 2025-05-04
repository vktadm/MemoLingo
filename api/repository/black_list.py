from redis.asyncio import Redis


class TokenBlackListRepository:
    def __init__(self, session: Redis):
        self.session = session

    async def add_token(self, token: str, expiration: int):
        print(token, 0, expiration)
        await self.session.set(token, 0, ex=expiration * 60)

    async def block_token(self, token: str):
        ttl = await self.session.ttl(token)
        if ttl != -2:
            await self.session.setex(token, ttl, 1)

    async def token_is_expired(self, token: str) -> bool:
        is_expired = await self.session.get(token)
        if not is_expired:
            return True
        return bool(int(is_expired.decode("utf-8")))
