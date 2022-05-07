from fastapi import FastAPI, Body, Depends
from model import PostSchema, UserSchema, UserLoginSchema
from auth.jwt_handler import signJWT, decodeJWT
from auth.jwt_bearer import jwtBearer
from db.session import SessionLocal, engine
from typing import List
from sqlalchemy.orm import Session
#from db import crud, models, schemas
import models
from db.init_db import init_db
from core.config import settings

from api.api_v1.api import api_router

posts = [
    {
        "id": 1,
        "title": "Post 1",
        "content": "This is post 1"
    }
]


app = FastAPI()
db = SessionLocal()
init_db(db)

#models.Base.metadata.create_all(bind=engine)



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@app.get("/", tags=["test"])
def home():
    return {"message": "Hello World"}

# @app.get("/posts", tags=["posts"])
# def get_post():
#     return {
#         "data": posts
#     }

# @app.get("/posts/{id}", tags=["posts"])
# def get_post_by_id(id: int):
#     if id > len(posts):
#         return {
#             "error": "Post not found"
#         }

#     for post in posts:
#         if post["id"] == id:
#             return {
#                 "data": post
#             }


# @app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
# def add_post(post: PostSchema):
#     post.id = len(posts) + 1
#     posts.append(post.dict())
#     return {
#         "info": "Post added",
#     }


# @app.post("/user/signup", tags=["user"])
# def user_signup(user: UserSchema = Body(default=None)):
#     users.append(user)

#     return signJWT(user.email)

# def check_user(data: UserLoginSchema):
#     for user in users:
#         if user.email == data.email and user.password == data.password:
#             return True
#     return False

# @app.post("/user/login", tags=["user"])
# def user_login(user: UserLoginSchema = Body(default=None)):
#     if check_user(user):
#         return signJWT(user.email)
#     return {
#         "error": "Invalid email or password"
#     }

app.include_router(api_router, prefix=settings.API_V1_STR)