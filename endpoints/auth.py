from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.user import User
from schemas.auth import UserRegister, TokenResponse, UserLogin
from services.auth import hash_password, verify_password, create_access_token, decode_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

@router.post('/v1/auth/register')
def auth_register(user: UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail='User already registered')
    
    existing_email = db.query(User).filter(User.email == user.email).first()

    if existing_email:
        raise HTTPException(status_code=400, detail='Email already registered')
    
    new_user = User(
        username = user.username,
        email = user.email,
        hashed_password = hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "username": new_user.username}




@router.post('/v1/auth/login')
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    existing_username = db.query(User).filter(User.username == form_data.username).first()

    if not existing_username:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    if not verify_password(form_data.password, existing_username.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": existing_username.username})
    return TokenResponse(access_token=token, token_type="bearer")