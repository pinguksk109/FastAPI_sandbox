
from fastapi import APIRouter, Depends, HTTPException, Query
from application.usecase.usage_usecase import UsageUsecase
from response.usage_response import UsageResponse
from request.usage_request import UsageRequest

router = APIRouter()

@router.get("/usage", response_model=UsageResponse)
async def get_usage(
    organization_id: str = Query(None, alias="organizationId"),
    user_id: str = Query(None, alias="userId"),
    usecase: UsageUsecase = Depends()
):
    if not organization_id or not organization_id.strip():
        raise HTTPException(status_code=400, detail="組織IDないよ")
    if not user_id or not user_id.strip():
        raise HTTPException(status_code=400, detail="ユーザーIDないよ")

    request = UsageRequest(organization_id=organization_id, user_id=user_id)
    return await usecase.execute(request)