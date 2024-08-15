from models.pydantic_models import PhoneDataModel
from repositories.redis_repo import AbstractRedisRepository


class PhoneDataRedisRepository(AbstractRedisRepository):
    async def get(self, key) -> PhoneDataModel | None:
        result = await self.async_pool.get(key)

        if not result:
            return None

        return PhoneDataModel(
            number=key,
            address=result
        )
