from fastapi import FastAPI, Body, Depends
from model import PostSchema, UserSchema, UserLoginSchema
from auth.jwt_handler import signJWT, decodeJWT
from auth.jwt_bearer import jwtBearer

posts = [
    {
        "id": 1,
        "title": "Post 1",
        "content": "This is post 1"
    }
]

users = [

]

app = FastAPI()

@app.get("/", tags=["test"])
def home():
    return {"message": "Hello World"}

@app.get("/posts", tags=["posts"])
def get_post():
    return {
        "data": posts
    }

@app.get("/posts/{id}", tags=["posts"])
def get_post_by_id(id: int):
    if id > len(posts):
        return {
            "error": "Post not found"
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post added",
    }


@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)

    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Invalid email or password"
    }
