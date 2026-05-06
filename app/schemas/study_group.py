from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class StudyGroupCreate(BaseModel):
    title: str
    description: Optional[str] = None
    max_members: int

class StudyGroupResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    max_members: int
    current_members: int
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}