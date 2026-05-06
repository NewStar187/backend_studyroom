from pydantic import BaseModel
from datetime import datetime

class ReservationCreate(BaseModel):
    room_id: int
    start_time: datetime
    end_time: datetime

class ReservationResponse(BaseModel):
    id: int
    room_id: int
    user_id: int
    start_time: datetime
    end_time: datetime
    created_at: datetime

    model_config = {"from_attributes": True}