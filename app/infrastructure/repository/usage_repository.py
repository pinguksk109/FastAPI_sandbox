class UsageRepository:
    async def get_limit(self, organization_id: str) -> int:
        return 100