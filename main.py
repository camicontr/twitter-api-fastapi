# Dependence
from schema import UserBase, User, UserLogin, UserRegister, Tweet
from models import Tweets, Users
from database import SessionLocal, engine

# Python
from typing import List

# FastApi
from fastapi import FastAPI
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi import Path

# Sqlalchemy
from sqlalchemy.orm import Session


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
    user: UserRegister = Body(...),
    db: Session = Depends(get_db)
    ):
    """
    Signup

    This path operation register a user in the app

    Parameters:
        - Request body parameter
            - user: UserRegister

    Return a dict with the basic user information
        - first_name: str
        - last_name: str
        - birth_date: date
    """
    db_user = Users(
        id=user.user_id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=user.password+"notreallyhashed",
        birth_date=user.birth_date
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

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
    pass

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
        description="This is the user ID. Its required"
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
    pass

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
    pass

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
    pass

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
        description="This is the user ID. Its required"
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
    pass

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
