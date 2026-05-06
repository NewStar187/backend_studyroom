from sqlalchemy.orm import Session
from app.models.study_group import StudyGroup
from app.models.application import Application

def get_groups(db: Session, skip: int = 0, limit: int = 20):
    return db.query(StudyGroup).order_by(
        StudyGroup.created_at.desc()
    ).offset(skip).limit(limit).all()

def get_group_by_id(db: Session, group_id: int):
    return db.query(StudyGroup).filter(StudyGroup.id == group_id).first()

def create_group(db: Session, group: StudyGroup):
    db.add(group)
    db.commit()
    db.refresh(group)
    return group

def delete_group(db: Session, group: StudyGroup):
    db.delete(group)
    db.commit()

def create_application(db: Session, application: Application):
    db.add(application)
    db.commit()
    db.refresh(application)
    return application

def get_application(db: Session, group_id: int, user_id: int):
    return db.query(Application).filter(
        Application.group_id == group_id,
        Application.user_id == user_id
    ).first()

def update_application_status(db: Session, application: Application, status: str):
    application.status = status
    db.commit()