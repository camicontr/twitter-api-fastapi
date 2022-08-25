# Dependence
from schema import UserBase, User, UserLogin, UserRegister, Tweet
from models import Tweets, Users
from database import SessionLocal, engine

# Python
from typing import List
from datetime import date

# FastApi
from fastapi import FastAPI
from fastapi import HTTPException
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
    if db_user is None:
        raise HTTPException(status_code=400, detail="Email or ID already registered")
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
def login(
    user: UserLogin = Body(...),
    db: Session = Depends(get_db)
):
    """
    Login a user

    This path operation login a user in the app

    Parameters:
        - Request body parameter
            - user: UserLogin

    Returns a json list with a user in the app, with the following keys: 
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    login = db.query(Users).filter(Users.email == user.email, Users.hashed_password == user.password).first()
    if login is None:
        raise HTTPException(status_code=404, detail="Login denied")
    return login

### Show all users
@app.get( # obteniendo informacion 
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users(
    db: Session = Depends(get_db)
    ):
    """
    Show all Users

    This path operation shows all users in the app

    Parameters: 
        -

    Returns a json list with all users in the app, with the following keys: 
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    users = db.query(Users).all()
    
    return users

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
        example="3fa15f64-5717-4562-b3fc-2c963f66afa6"
        ),
    db: Session = Depends(get_db)
):
    """
    This path operation shows a user in the app

    Parameters:
        Path parameter
        - user_id: specify id for user
    
    Returns a json list with a user in the app, with the following keys:
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    user = db.query(Users).filter(Users.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user(
    user_id: str = Path(
        ...,
        min_length=36,
        max_length=36,
        title="User ID",
        description="This is the user ID. Its required",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa7"
        ),
    db: Session = Depends(get_db)
):
    """
    This path operation delete a user in the app

    Parameters:
        Path parameter
        - user_id: specify id for user
    
    Returns a json list with a deleted user in the app, with the following keys:
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    db.query(Users).filter(Users.id == user_id).delete(synchronize_session="fetch")
    db.commit()
    return {"user id deleted":user_id}


### Update a user
@app.put( 
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user(
    user_id: str = Path(
        ...,
        min_length=36,
        max_length=36,
        title="User ID",
        description="This is the user ID. Its required",
        example="3fa85f64-5717-4562-b3fc-2c963f68afa6"
        ),
    hashed_password_up: str = Body(
        ...,
        min_length=8,
        max_length=64),
    birth_date_up: date = Body(...),
    db: Session = Depends(get_db)
):
    """
    This path operation update the password and birth date in the app

    Parameters:
        Path parameter
        - user_id: specify id for user
        Body parameter
        - hashed_password_up: new password
        - birth_date_up: new birth date
    
    Returns a json list with a deleted user in the app, with the following keys:
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    db.query(Users).filter(Users.id == user_id).update(
        {"hashed_password":hashed_password_up,
         "birth_date":birth_date_up
        }, synchronize_session="fetch"
        )
    db.commit()
    user_up = show_a_user(user_id, db)
    return user_up

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
