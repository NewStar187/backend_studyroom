from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories import room_repo
from app.schemas.room import RoomResponse

router = APIRouter()

@router.get("/rooms")
def get_rooms(db: Session = Depends(get_db)):
    return room_repo.get_rooms(db)

@router.get("/rooms/{room_id}", response_model=RoomResponse)
def get_room(room_id: int, db: Session = Depends(get_db)):
    return room_repo.get_room_by_id(db, room_id)