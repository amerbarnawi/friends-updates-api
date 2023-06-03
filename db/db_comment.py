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
