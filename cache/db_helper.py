import redis
from config import settings


def get_redis_connection() -> redis.Redis:
    return redis.Redis(
        host=settings.cache.host,
        port=settings.cache.port,
        db=settings.cache.db,
    )
