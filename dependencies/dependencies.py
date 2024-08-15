import redis.asyncio as redis

import config
from repositories.phone_repository import PhoneDataRedisRepository
from services.phone_data_service import PhoneDataService


def get_redis_async_pool() -> redis.Redis:
    pool = redis.ConnectionPool.from_url(f"redis://@{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}")
    client = redis.Redis.from_pool(pool)
    return client


def get_phone_data_repo():
    pool = get_redis_async_pool()
    repository = PhoneDataRedisRepository(pool)
    return repository


def get_phone_data_service():
    repo = get_phone_data_repo()
    service = PhoneDataService(repo)
    return service
