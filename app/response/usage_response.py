from pydantic import BaseModel

class UsageResponse(BaseModel):
    count: int
    limit: int