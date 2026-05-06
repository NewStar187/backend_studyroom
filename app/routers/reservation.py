from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.reservation import ReservationCreate, ReservationResponse
from app.repositories import reservation_repo, room_repo
from app.models.reservation import Reservation
from app.core.deps import get_current_user
from fastapi import HTTPException

router = APIRouter()

@router.post("/reservations", response_model=ReservationResponse)
def create_reservation(
    data: ReservationCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    room = room_repo.get_room_by_id(db, data.room_id)
    if not room:
        raise HTTPException(status_code=404, detail="스터디룸을 찾을 수 없습니다")

    conflict = reservation_repo.get_overlapping_reservation(
        db, data.room_id, data.start_time, data.end_time
    )
    if conflict:
        raise HTTPException(status_code=409, detail="해당 시간대에 이미 예약이 있습니다")

    reservation = Reservation(
        room_id=data.room_id,
        user_id=current_user.id,
        start_time=data.start_time,
        end_time=data.end_time
    )
    return reservation_repo.create_reservation(db, reservation)

@router.get("/reservations/my")
def get_my_reservations(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return reservation_repo.get_reservations_by_user(db, current_user.id)

@router.delete("/reservations/{reservation_id}")
def delete_reservation(
    reservation_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    from app.models.reservation import Reservation as R
    r = db.query(R).filter(R.id == reservation_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="예약을 찾을 수 없습니다")
    if r.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="취소 권한이 없습니다")
    reservation_repo.delete_reservation(db, r)
    return {"message": "예약이 취소되었습니다"}