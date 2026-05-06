from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.comment import CommentCreate, CommentResponse
from app.repositories import comment_repo
from app.models.comment import Comment
from app.core.deps import get_current_user
from fastapi import HTTPException

router = APIRouter()

@router.get("/posts/{post_id}/comments")
def get_comments(post_id: int, db: Session = Depends(get_db)):
    return comment_repo.get_comments_by_post(db, post_id)

@router.post("/posts/{post_id}/comments", response_model=CommentResponse)
def create_comment(
    post_id: int,
    data: CommentCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    comment = Comment(
        post_id=post_id,
        user_id=current_user.id,
        content=data.content,
        parent_comment_id=data.parent_comment_id
    )
    return comment_repo.create_comment(db, comment)

@router.delete("/comments/{comment_id}")
def delete_comment(
    comment_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    comment = comment_repo.get_comment_by_id(db, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="댓글을 찾을 수 없습니다")
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="삭제 권한이 없습니다")
    comment_repo.delete_comment(db, comment)
    return {"message": "삭제되었습니다"}