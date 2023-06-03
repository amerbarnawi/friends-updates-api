from typing import List
from pydantic import BaseModel
from datetime import datetime

# User schemas


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config():
        orm_mode = True

# ================================================
# Post schemas
# ================================================

# For post display


class User(BaseModel):
    id: int
    username: str

    class Config():
        orm_mode = True


class CommentDisplay(BaseModel):
    id: int
    text: str
    username: str
    timestamp: datetime

    class Config():
        orm_mode = True


class PostBase(BaseModel):
    title: str
    content: str
    img_url: str
    creater_id: int


class PostDisplay(BaseModel):
    title: str
    content: str
    img_url: str
    publish_date: datetime
    user: User
    comments: List[CommentDisplay]

    class Config():
        orm_mode = True


class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int


# ================================================
# AUTHENTICATION
# ================================================


class UserAuth(BaseModel):
    id: int
    username: str
    email: str
