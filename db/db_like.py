from fastapi import HTTPException, status
from db.models import DbLike, DbPost
from routers.schemas import LikeBase
from sqlalchemy.orm.session import Session


def update_like(db: Session, request: LikeBase):

    post = db.query(DbPost).filter(DbPost.id == request.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id:{request.post_id} is not found!')
    like = db.query(DbLike).filter(DbLike.post_id == request.post_id).filter(
        DbLike.username == request.username).first()
    if like:
        return delete_like(db, like.id)

    new_like = DbLike(
        username=request.username,
        post_id=request.post_id
    )
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like


def delete_like(db: Session, like_id: int):
    like = db.query(DbLike).filter(DbLike.id == like_id).first()
    db.delete(like)
    db.commit()
    return {"details": 'Like is deleted!'}
