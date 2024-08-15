from abc import ABC, abstractmethod


class AbstractKeyValueRepository(ABC):
    @abstractmethod
    async def set(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def get(self, *args, **kwargs):
        raise NotImplemented
