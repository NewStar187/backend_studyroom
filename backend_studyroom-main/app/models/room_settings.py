from sqlalchemy import Column, Integer, Time, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class RoomSettings(Base):
    __tablename__ = "room_settings"

    id            = Column(Integer, primary_key=True)
    room_id       = Column(Integer, ForeignKey("study_rooms.id"), nullable=False)
    open_time     = Column(Time, nullable=False)   # 운영 시작 시간
    close_time    = Column(Time, nullable=False)   # 운영 종료 시간
    slot_duration = Column(Integer, nullable=False, default=60)  # 예약 단위 (분)
    created_at    = Column(DateTime(timezone=True), server_default=func.now())