from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import (
    RegisterRequest, LoginRequest,
    ReactivateRequest, TokenResponse
)
from app.services import auth_service
from app.core.deps import get_current_user

router = APIRouter()

@router.post("/register", response_model=TokenResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    token = auth_service.register(db, data)
    return {"access_token": token}

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    token = auth_service.login(db, data.email, data.password)
    return {"access_token": token}

@router.delete("/delete")
def delete_account(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    auth_service.soft_delete(db, current_user)
    return {"message": "계정이 삭제되었습니다. 30일 내 복구 가능합니다"}

@router.post("/reactivate", response_model=TokenResponse)
def reactivate(data: ReactivateRequest, db: Session = Depends(get_db)):
    token = auth_service.reactivate(db, data.email, data.password)
    return {"access_token": token}