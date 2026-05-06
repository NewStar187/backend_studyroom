from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    nickname: str
    role: str
    created_at: datetime

    model_config = {"from_attributes": True}