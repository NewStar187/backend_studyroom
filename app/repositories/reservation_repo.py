from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.models.reservation import Reservation
from datetime import datetime

def get_reservations_by_room(db: Session, room_id: int):
    return db.query(Reservation).filter(
        Reservation.room_id == room_id
    ).order_by(Reservation.start_time.asc()).all()

def get_reservations_by_user(db: Session, user_id: int):
    return db.query(Reservation).filter(
        Reservation.user_id == user_id
    ).order_by(Reservation.start_time.asc()).all()

def get_overlapping_reservation(db: Session, room_id: int,
                                 start_time: datetime, end_time: datetime):
    return db.query(Reservation).filter(
        and_(
            Reservation.room_id == room_id,
            Reservation.start_time < end_time,
            Reservation.end_time > start_time,
        )
    ).first()

def create_reservation(db: Session, reservation: Reservation):
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation

def delete_reservation(db: Session, reservation: Reservation):
    db.delete(reservation)
    db.commit()