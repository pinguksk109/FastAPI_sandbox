from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from usecases.zipcode_usecase import ZipcodeUsecase
from repository.zipcode_repository import ZipcodeRepository

router = APIRouter()

class Address(BaseModel):
    address1: str
    address2: str
    address3: str
    kana1: str
    kana2: str
    kana3: str
    prefcode: str
    zipcode: str

class ZipcodeResponse(BaseModel):
    message: str
    results: List[Address]
    status: int

def get_zipcode_usecase() -> ZipcodeUsecase:
    repository = ZipcodeRepository()
    return ZipcodeUsecase(repository)

@router.get("/addresses/{zipcode}", response_model=ZipcodeResponse)
async def get_address(zipcode: str, usecase: ZipcodeUsecase = Depends(get_zipcode_usecase)):
    print(zipcode)
    result = await usecase.get_address_by_zipcode(zipcode)
    if result is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return result