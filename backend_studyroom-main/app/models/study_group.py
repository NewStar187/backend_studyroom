from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base

class StudyGroup(Base):
    __tablename__ = "study_groups"

    id              = Column(Integer, primary_key=True)
    user_id         = Column(Integer, nullable=False)
    title           = Column(String(200), nullable=False)
    description     = Column(Text)
    max_members     = Column(Integer, nullable=False, default=5)
    current_members = Column(Integer, nullable=False, default=1)
    # 모집중 / 모집완료 / 종료
    status          = Column(String(20), nullable=False, default="모집중", server_default="모집중")
    created_at      = Column(DateTime(timezone=True), server_default=func.now())
    updated_at      = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())