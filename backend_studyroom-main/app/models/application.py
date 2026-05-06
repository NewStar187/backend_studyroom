from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Application(Base):
    __tablename__ = "applications"

    id         = Column(Integer, primary_key=True)
    group_id   = Column(Integer, ForeignKey("study_groups.id"), nullable=False)
    user_id    = Column(Integer, ForeignKey("users.id"), nullable=False)
    # 대기 / 수락 / 거절
    status     = Column(String(20), nullable=False, default="대기", server_default="대기")
    created_at = Column(DateTime(timezone=True), server_default=func.now())