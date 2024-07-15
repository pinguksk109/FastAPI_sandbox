from typing import Optional
from repository.zipcode_repository import ZipcodeRepository

class ZipcodeUsecase:
    def __init__(self, repository: ZipcodeRepository):
        self.repository = repository

    async def get_address_by_zipcode(self, zipcode: str) -> Optional[dict]:
        return await self.repository.get_address_by_zipcode(zipcode)