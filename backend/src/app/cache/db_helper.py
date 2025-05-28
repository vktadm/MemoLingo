from redis.asyncio import Redis

from backend.src.app.settings import settings


async def get_redis_session() -> Redis:
    session = Redis(
        host=settings.cache.host,
        port=settings.cache.port,
        db=settings.cache.db,
    )
    async with session as s:
        yield s
        await s.close()
