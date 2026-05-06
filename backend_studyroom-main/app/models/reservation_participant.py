from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class ReservationParticipant(Base):
    __tablename__ = "reservation_participants"

    id             = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey("reservations.id"), nullable=False)
    user_id        = Column(Integer, ForeignKey("users.id"), nullable=False)
    joined_at      = Column(DateTime(timezone=True), server_default=func.now())