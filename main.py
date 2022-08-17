# Python
from uuid import UUID
from datetime import datetime, date
from typing import Optional, List

# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# FastApi
from fastapi import FastAPI
from fastapi import status


app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)


class User(UserBase):
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


class UserLogin(UserBase):
        password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        max_length=256,
        min_length=1)
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)


# Path operations

@app.get(
    path="/")
def home():
    return {"Twitter API": "Working!"}

## Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tag=["Users"]
)
def signup():
    pass


@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tag=["Users"]
)
def login():
    pass


@app.get( # obteniendo informacion 
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tag=["Users"]
)
def show_all_users():
    pass


@app.get( # obteniendo informacion 
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tag=["Users"]
)
def show_a_user():
    pass


@app.delete( # peticion de eliminacion
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tag=["Users"]
)
def delete_a_user():
    pass


@app.put( 
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tag=["Users"]
)
def update_a_user():
    pass
