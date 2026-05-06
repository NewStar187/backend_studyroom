from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RoomResponse(BaseModel):
    id: int
    name: str
    capacity: int
    created_at: datetime

    model_config = {"from_attributes": True}

class RoomSettingsUpdate(BaseModel):
    open_time: str    # "09:00"
    close_time: str   # "22:00"
    slot_duration: int