from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from transformers import pipeline

#from app import crud, models, schemas
from app import schemas
from app import models
from app.api import deps
from app.core.config import settings
#from utils import send_new_account_email

router = APIRouter()

@router.post("/", response_model=List[schemas.PredictionRequest])
def classify_text() -> Any:
    """
    """
    users = []
    return users