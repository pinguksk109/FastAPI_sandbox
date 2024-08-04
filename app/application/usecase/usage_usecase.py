from fastapi import Depends
from infrastructure.repository.dynamodb_repository import DynamoDBRepository
from infrastructure.repository.usage_repository import UsageRepository
from domain.usage_info import UsageInfo
from response.usage_response import UsageResponse
from request.usage_request import UsageRequest

class UsageUsecase:
    def __init__(self, dynamodb_repository: DynamoDBRepository = Depends(), usage_repository: UsageRepository = Depends()):
        self.dynamodb_repository = dynamodb_repository
        self.usage_repository = usage_repository

    async def execute(self, request: UsageRequest) -> UsageResponse:
        data = await self.dynamodb_repository.get_mock_data(request.organization_id)
        limit = await self.usage_repository.get_limit(request.organization_id)
        usage_info = UsageInfo(limit=limit, row=data)
        count = usage_info.get_count()
        return UsageResponse(count=count, limit=limit)