from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommentCreate(BaseModel):
    content: str
    parent_comment_id: Optional[int] = None  # 대댓글이면 부모 id

class CommentResponse(BaseModel):
    id: int
    post_id: int
    user_id: int
    parent_comment_id: Optional[int]
    content: str
    created_at: datetime

    model_config = {"from_attributes": True}