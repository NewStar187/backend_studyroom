from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class PostImage(Base):
    __tablename__ = "post_images"

    id         = Column(Integer, primary_key=True)
    post_id    = Column(Integer, ForeignKey("posts.id"), nullable=False)
    image_url  = Column(Text, nullable=False)       # Supabase Storage URL
    order_num  = Column(Integer, nullable=False, default=0)  # 이미지 순서
    created_at = Column(DateTime(timezone=True), server_default=func.now())