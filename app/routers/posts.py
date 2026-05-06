from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.schemas.post import PostCreate, PostUpdate, PostResponse
from app.services import post_service
from app.core.deps import get_current_user

router = APIRouter()

@router.get("/posts")
def get_posts(
    skip: int = 0,
    limit: int = 20,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return post_service.get_posts(db, skip, limit, search)

@router.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return post_service.get_post(db, post_id)

@router.post("/posts", response_model=PostResponse)
def create_post(
    data: PostCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return post_service.create_post(db, current_user.id, data)

@router.put("/posts/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    data: PostUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return post_service.update_post(db, post_id, current_user.id, data)

@router.delete("/posts/{post_id}")
def delete_post(
    post_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    post_service.delete_post(db, post_id, current_user.id)
    return {"message": "삭제되었습니다"}