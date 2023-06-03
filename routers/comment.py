from typing import List
from fastapi import APIRouter, Depends
from auth.oauth2 import get_current_user
from db.database import get_db
from sqlalchemy.orm.session import Session
from routers.schemas import CommentBase, CommentDisplay, UserAuth
from db import db_comment

router = APIRouter(
    prefix='/comment',
    tags=['Comments']
)


@router.post('', response_model=CommentDisplay)
def create_comment(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_comment.create_comment(db, request)


@router.get('/all-comments', response_model=List[CommentDisplay])
def get_all_comments(db: Session = Depends(get_db)):
    return db_comment.get_all_comments(db)


@router.delete('/{id}')
def delete_comment(id: str, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_comment.delete_comment(db, id, current_user.username)
