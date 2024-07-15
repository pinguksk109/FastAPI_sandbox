import aiohttp
from typing import Optional

class ZipcodeRepository:
    async def get_address_by_zipcode(self, zipcode: str) -> Optional[dict]:
        url = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data['status'] == 200 and data['results']:
                        return data
        return None
