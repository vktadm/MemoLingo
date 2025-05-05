from redis import asyncio as redis

# import redis
from app.config import settings


async def get_redis_connection() -> redis.Redis:
    return redis.Redis(
        host=settings.cache.host,
        port=settings.cache.port,
        db=settings.cache.db,
    )
