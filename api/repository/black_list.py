from redis.asyncio import Redis


class TokenBlackListRepository:
    def __init__(self, session: Redis):
        self.session = session

    async def add_token(self, token: str, expiration: int):
        async with self.session as s:
            await s.set(token, 0, ex=expiration * 60)

    async def block_token(self, token: str):
        async with self.session as s:
            ttl = await s.ttl(token)
            if ttl != -2:
                await s.setex(token, ttl, 1)

    async def token_is_expired(self, token: str) -> bool:
        async with self.session as s:
            is_expired = await s.get(token)
        if not is_expired:
            return True
        return bool(int(is_expired.decode("utf-8")))
