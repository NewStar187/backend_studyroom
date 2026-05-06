from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostCreate(BaseModel):
    title: str
    content: str

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class PostResponse(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    view_count: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}