from fastapi import FastAPI, Body, Depends
from app.auth.jwt_handler import signJWT, decodeJWT
from app.auth.jwt_bearer import jwtBearer
from app.db.session import SessionLocal, engine
from typing import List
from sqlalchemy.orm import Session
#from db import crud, models, schemas
import app.models
from app.db.init_db import init_db
from app.core.config import settings

from app.api.api_v1.api import api_router

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


@app.get("/", tags=["test"])
def home():
    return {"message": "Hello World"}


app.include_router(api_router, prefix=settings.API_V1_STR)