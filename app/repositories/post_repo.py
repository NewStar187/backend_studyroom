from sqlalchemy.orm import Session
from app.models.post import Post
from typing import Optional

def get_posts(db: Session, skip: int = 0, limit: int = 20, search: Optional[str] = None):
    q = db.query(Post)
    if search:
        q = q.filter(Post.title.ilike(f"%{search}%"))
    return q.order_by(Post.created_at.desc()).offset(skip).limit(limit).all()

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: Session, post: Post):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def update_post(db: Session, post: Post):
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post: Post):
    db.delete(post)
    db.commit()

def increment_view(db: Session, post: Post):
    post.view_count += 1
    db.commit()