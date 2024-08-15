from models.pydantic_models import PhoneDataModel
from repositories.phone_repository import PhoneDataRedisRepository


class PhoneDataService:
    def __init__(self, phone_data_repo: PhoneDataRedisRepository):
        self.phone_data_repo = phone_data_repo

    async def get_data_by_number(self, phone_number: str) -> PhoneDataModel:
        data = await self.phone_data_repo.get(phone_number)
        return data

    async def add_new_phone_data(self, data: PhoneDataModel):
        """
        Here we can add an error if number already exists,
        but I think it is not necessary since the repository is key-value,
        and we just rewrite existing file
        """
        await self.phone_data_repo.set(
            key=data.number,
            value=data.address
        )

    async def update_phone_data(self, data: PhoneDataModel):
        await self.add_new_phone_data(data)
