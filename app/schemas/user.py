from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    answers: str
    password: str
    created_at: datetime = datetime.now()


class UserActivated(UserBase):
    id: int
    is_active: bool
    email: EmailStr


class User(UserBase):
    id: int
    answers: str
    created_at: datetime = None

    class Config:
        orm_mode = True
