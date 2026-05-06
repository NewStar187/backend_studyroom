from sqlalchemy.orm import Session
from app.models.notification import Notification

def create(db: Session, notification: Notification):
    db.add(notification)
    db.commit()

def get_by_user(db: Session, user_id: int):
    return db.query(Notification).filter(
        Notification.user_id == user_id
    ).order_by(Notification.created_at.desc()).all()

def mark_as_read(db: Session, notification_id: int, user_id: int):
    n = db.query(Notification).filter(
        Notification.id == notification_id,
        Notification.user_id == user_id
    ).first()
    if n:
        n.is_read = True
        db.commit()