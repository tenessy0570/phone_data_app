import typing
from abc import abstractmethod

from redis.asyncio import Redis

from repositories.base import AbstractKeyValueRepository


class AbstractRedisRepository(AbstractKeyValueRepository):
    def __init__(self, redis_async_pool: Redis):
        self.async_pool = redis_async_pool

    async def set(self, key: typing.Any, value: typing.Any):
        await self.async_pool.set(key, value)

    @abstractmethod
    async def get(self, key):
        raise NotImplemented
