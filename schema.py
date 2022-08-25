# Python
from uuid import UUID
from datetime import datetime, date
from typing import Optional

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    class Config:
        orm_mode = True


class User(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)
    class Config:
        orm_mode = True


class UserRegister(UserBase, User):
    email: EmailStr = Field(...)
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )


class Tweet(BaseModel):
    content: str = Field(
        ...,
        max_length=256,
        min_length=1)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    user_id: UUID = Field(...)
    class Config:
        orm_mode = True


class TweetPost(Tweet):
    tweet_id: UUID = Field(...)
