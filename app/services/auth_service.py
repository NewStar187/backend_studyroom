from datetime import datetime, timezone
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.repositories import user_repo
from app.models.user import User
from app.core.jwt import create_access_token
from app.core.exceptions import (
    DeactivatedAccountError,
    ExpiredRecoveryError
)
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def register(db: Session, data) -> str:
    if user_repo.get_user_by_email(db, data.email):
        raise HTTPException(status_code=409, detail="이미 사용 중인 이메일입니다")
    user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password),
        nickname=data.nickname,
    )
    created = user_repo.create_user(db, user)
    return create_access_token(created.id)

def login(db: Session, email: str, password: str) -> str:
    user = user_repo.get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 틀렸습니다")

    if not user.is_active:
        now = datetime.now(timezone.utc)
        deleted = user.deleted_at.replace(tzinfo=timezone.utc)
        days = (now - deleted).days
        if days <= 30:
            raise DeactivatedAccountError()
        else:
            raise HTTPException(status_code=401, detail="복구 기간이 만료된 계정입니다")

    return create_access_token(user.id)

def soft_delete(db: Session, user: User):
    user.is_active = False
    user.deleted_at = datetime.now(timezone.utc)
    db.commit()

def reactivate(db: Session, email: str, password: str) -> str:
    user = user_repo.get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="인증 실패")

    now = datetime.now(timezone.utc)
    deleted = user.deleted_at.replace(tzinfo=timezone.utc)
    if (now - deleted).days > 30:
        raise ExpiredRecoveryError()

    user.is_active = True
    user.deleted_at = None
    db.commit()
    return create_access_token(user.id)