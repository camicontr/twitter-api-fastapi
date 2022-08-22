# Python
import json
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
from fastapi import Body
from fastapi import Path

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


class UserRegister(User):
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
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Auxiliar functions

def save_json(name_json:str, object):
    with open(name_json+".json", "r+", encoding="utf-8") as f:
        result = json.loads(f.read())
        object_dict = object.dict()
        result.append(object_dict)
        f.seek(0)
        json.dump(result, f, default=str, indent=4)


def save_json(name_json:str, object):
    with open(name_json+".json", "r+", encoding="utf-8") as f:
        json_list = json.loads(f.read())
        for object_dict in json_list:
            tweets["tweet_id"] = str(tweets["tweet_id"])
            if tweets["tweet_id"] == tweet_id:
                return  

# Path operations

## Users

### Resgister a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(
    user: UserRegister = Body(...)
    ):
    """
    Signup

    This path operation register a user in the app

    Parameters:
        - Request body parameter
            - user: UserRegister

    Return a json with the basic user information
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    save_json("users", user)
    return user

### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

### Show all users
@app.get( # obteniendo informacion 
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    """
    This path operation shows all users in the app
    Parameters: 
        -
    Returns a json list with all users in the app, with the following keys: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json", "r", encoding="utf-8") as f:
        result = json.loads(f.read())
        return result

### Show a user
@app.get( # obteniendo informacion 
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user(
    user_id: str = Path(
        ...,
        min_length=36,
        max_length=36,
        title="User ID",
        description="This is the user ID. Its required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa7"
        )
):
    """
    This path operation shows a user in the app

    Parameters:
        Path parameter
        - user_id: specify id for user
    
    Returns a json list with a user in the app, with the following keys: 
        - user_id: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json", "r", encoding="utf-8") as f:
        users_list = json.loads(f.read())
        for users in users_list:
            users["user_id"] = str(users["user_id"])
            if users["user_id"] == user_id:
                return users

### Delete a user
@app.delete( # peticion de eliminacion
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

### Update a user
@app.put( 
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass

## Tweet

### Show all tweets
@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all Tweets",
    tags=["Tweets"]
)
def home():
    """
    Home

    This path operation shows all tweets in the app
    
    Parameters
        -

    Returns a json list with all tweets in the app, with the following keys: 
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        result = json.loads(f.read())
        return result

### Post a tweet
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post(
    tweet: Tweet = Body(...)
):
    """
    Post a tweet

    This path operation post a tweet in the app

    Parameters:
        - Request body parameter
            - tweet: Tweet

    Return a json with the basic tweet information
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    save_json("tweets", tweet)
    return tweet

### Show a tweet
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a tweet",
    tags=["Tweets"]
)
def show_a_tweet(
    tweet_id: str = Path(
        ...,
        min_length=36,
        max_length=36,
        title="Tweet ID",
        description="This is the user ID. Its required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa7"
        )
):
    """
    This path operation shows a tweet in the app

    Parameters:
        Path parameter
        - tweet_id: tweet id
    
    Return a json with the basic tweet information
        - tweet_id: UUID
        - content: str
        - created_at: datetime
        - updated_at: Optional[datetime]
        - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        tweets_list = json.loads(f.read())
        for tweets in tweets_list:
            tweets["tweet_id"] = str(tweets["tweet_id"])
            if tweets["tweet_id"] == tweet_id:
                return tweets

### Delete a tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

### Update a tweet
@app.put( # put para actualizar 
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass
