from sqlalchemy.orm import Session
from app.repositories import post_repo
from app.models.post import Post
from fastapi import HTTPException
from typing import Optional

def get_posts(db: Session, skip: int = 0, limit: int = 20, search: Optional[str] = None):
    return post_repo.get_posts(db, skip, limit, search)

def get_post(db: Session, post_id: int):
    post = post_repo.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")
    post_repo.increment_view(db, post)
    return post

def create_post(db: Session, user_id: int, data) -> Post:
    post = Post(user_id=user_id, title=data.title, content=data.content)
    return post_repo.create_post(db, post)

def update_post(db: Session, post_id: int, user_id: int, data) -> Post:
    post = post_repo.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")
    if post.user_id != user_id:
        raise HTTPException(status_code=403, detail="수정 권한이 없습니다")
    if data.title is not None:
        post.title = data.title
    if data.content is not None:
        post.content = data.content
    return post_repo.update_post(db, post)

def delete_post(db: Session, post_id: int, user_id: int):
    post = post_repo.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다")
    if post.user_id != user_id:
        raise HTTPException(status_code=403, detail="삭제 권한이 없습니다")
    post_repo.delete_post(db, post)