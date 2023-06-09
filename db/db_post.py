from fastapi import HTTPException, status
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost
import datetime


def create_post(db: Session, request: PostBase):
    new_post = DbPost(
        title=request.title,
        content=request.content,
        img_url=request.img_url,
        publish_date=datetime.datetime.now(),
        creater_id=request.creater_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db: Session):
    return db.query(DbPost).all()


def delete_post(db: Session, id: int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id:{id} is not found!')
    if post.creater_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only post creater can delete post.')
    db.delete(post)
    db.commit()
    return {"details": 'Your post has been deleted successfully!'}
