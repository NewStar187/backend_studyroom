from sqlalchemy.orm import Session
from app.models.notification import Notification
from app.repositories import notification_repo

def notify(db: Session, user_id: int, type: str, message: str):
    n = Notification(user_id=user_id, type=type, message=message)
    notification_repo.create(db, n)