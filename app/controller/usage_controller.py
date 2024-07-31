
from fastapi import APIRouter, Query
from app.request.usage_request import UsageRequest

router = APIRouter()

@router.get("/usage", response_model=UsageResponse)
async def get_usage(
    organization_id: str = Query(..., alias="organizationId"),
    user_id: str = Query(..., alias="userId"),
    usecase: UsageUseCase = Depends()
):
    request = UsageRequest(organization_id=organization_id, user_id=user_id)
    return await usecase.execute(request)