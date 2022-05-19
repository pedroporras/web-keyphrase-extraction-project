from fastapi import APIRouter

from .endpoints import users
from .endpoints import sentiment_analysis

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(sentiment_analysis.router, prefix="/sentiment_analysis", tags=["Sentiment Analysis"])
