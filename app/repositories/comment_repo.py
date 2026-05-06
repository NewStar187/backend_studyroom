from sqlalchemy.orm import Session
from app.models.comment import Comment

def get_comments_by_post(db: Session, post_id: int):
    return db.query(Comment).filter(
        Comment.post_id == post_id
    ).order_by(Comment.created_at.asc()).all()

def create_comment(db: Session, comment: Comment):
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comment_by_id(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def delete_comment(db: Session, comment: Comment):
    db.delete(comment)
    db.commit()