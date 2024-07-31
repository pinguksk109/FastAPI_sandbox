from pydantic import BaseModel

class UsageRequest(BaseModel):
    organization_id: str
    user_id: str