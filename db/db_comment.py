from fastapi import HTTPException, status
from db.models import DbComment
from routers.schemas import CommentBase
from sqlalchemy.orm.session import Session
import datetime


def create_comment(db: Session, request: CommentBase):
    new_comment = DbComment(
        text=request.text,
        username=request.username,
        timestamp=datetime.datetime.now(),
        post_id=request.post_id,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all_comments(db: Session):
    return db.query(DbComment).all()


def delete_comment(db: Session, comment_id, username):
    comment = db.query(DbComment).filter(DbComment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Comment by id:{comment_id} is not found!')
    if comment.username != username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only comment creater can delete the comment!')

    db.delete(comment)
    db.commit()
    return {"details": 'Comment has been deleted successfully!'}
