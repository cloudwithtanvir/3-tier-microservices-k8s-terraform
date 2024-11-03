from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import User
from database import get_db

router = APIRouter()

@router.post("/users/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    db_user = User(username=username, email=email)
    db_user.set_password(password)  # Hash the password before saving
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"user_id": db_user.id, "username": db_user.username, "email": db_user.email}

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
