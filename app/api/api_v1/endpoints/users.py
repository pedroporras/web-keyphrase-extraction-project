from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

#from app import crud, models, schemas
import schemas
import models
from api import deps
from core.config import settings
#from utils import send_new_account_email

router = APIRouter()

# @router.get("/", response_model=List[schemas.User])
# def read_users(
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     current_user: models.User = Depends(deps.get_current_active_superuser),
# ) -> Any:
@router.get("/", response_model=List[schemas.User])
def read_users() -> Any:
    """
    Retrieve users.
    """
    #users = crud.user.get_multi(db, skip=skip, limit=limit)
    users = []
    return users