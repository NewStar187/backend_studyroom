from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.jwt import decode_token
from app.repositories import user_repo
from app.core.exceptions import InvalidTokenError, PermissionDeniedError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_token(token)          # 토큰 검증
    user = user_repo.get_user_by_id(db, user_id)
    if not user or not user.is_active:     # 탈퇴 여부 체크
        raise InvalidTokenError()
    return user

def get_admin_user(current_user = Depends(get_current_user)):
    if current_user.role != "admin":
        raise PermissionDeniedError()
    return current_user