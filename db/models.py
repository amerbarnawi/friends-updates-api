from .database import Base
from sqlalchemy import Column, ForeignKey, String, Integer, column, DateTime
from sqlalchemy.orm import relationship


# User model

class DbUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DbPost', back_populates='user')

# =================================================
# Post model


class DbPost(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    img_url = Column(String)
    publish_date = Column(DateTime)
    creater_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser', back_populates='items')
