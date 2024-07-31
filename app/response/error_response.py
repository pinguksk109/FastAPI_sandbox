from pydantic import BaseModel

class ErrorResponse(BaseModel):
    status_code: int
    user_message: str
    dev_message: str
