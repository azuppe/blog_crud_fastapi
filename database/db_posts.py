from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
import datetime
from database.models import Post
from fastapi import HTTPException,  status


def create(db:Session, request:PostBase):
    new_post = Post(
        image_url=request.image_url,
        title=request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now(),
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def fetchAll(db:Session):
    return db.query(Post).all()

def deletePost(id:int, db:Session):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    db.delete(post)
    db.commit()
    return post