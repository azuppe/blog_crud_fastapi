from .database import Base
from sqlalchemy import  Column, Boolean, Integer, String, DateTime

class Post(Base):
    __tablename__ ="posts"
    id = Column(Integer, primary_key = True, index = True )
    image_url = Column(String)
    title = Column(String)
    content = Column(String)
    creator = Column(String)
    timestamp= Column(DateTime)
    