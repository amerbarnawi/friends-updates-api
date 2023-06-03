import random
from fastapi import APIRouter, Depends, UploadFile, status, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from routers.schemas import PostBase, PostDisplay, UserAuth
from db.database import get_db
from db import db_post
from typing import List
import string
import random
import shutil


router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    new_post = db_post.create_post(db, request)
    return new_post


@router.get('/all-posts', response_model=List[PostDisplay])
def get_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)


@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(3))
    new = f'_{random_string}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}
