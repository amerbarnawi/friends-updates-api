from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from routers.schemas import LikeBase, LikeDisplay, UserAuth
from db import db_like

router = APIRouter(
    prefix='/like',
    tags=['Like']
)


@router.post('')
def update_like(request: LikeBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_like.update_like(db, request)
