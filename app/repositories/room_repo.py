from sqlalchemy.orm import Session
from app.models.study_room import StudyRoom

def get_rooms(db: Session):
    return db.query(StudyRoom).all()

def get_room_by_id(db: Session, room_id: int):
    return db.query(StudyRoom).filter(StudyRoom.id == room_id).first()