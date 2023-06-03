from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from db.database import get_db
from routers.schemas import LikeBase, LikeDisplay
from db import db_like

router = APIRouter(
    prefix='/like',
    tags=['Like']
)


@router.post('')
def update_like(request: LikeBase, db: Session = Depends(get_db)):
    return db_like.update_like(db, request)
