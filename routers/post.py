from fastapi import APIRouter, Depends, UploadFile, File
from .schemas import PostBase, postDisplay
from sqlalchemy.orm import Session
from dependencies import get_db
from database import  db_posts
import string
import random
import shutil

router = APIRouter(
    prefix="/post",
    tags=['post']
)

@router.post('')
def create (request:PostBase, db:Session= Depends(get_db)):
    return db_posts.create(db, request)
    
@router.get('/posts')
def posts ( db:Session= Depends(get_db)):
    return db_posts.fetchAll(db)

@router.delete('')
def deletePost(id:int, db:Session = Depends(get_db)):
    return db_posts.deletePost(id, db)
    
@router.post('/image')
def upload_image(image:UploadFile = File(...)):
    letters =string.ascii_letters
    rand_str = ''.join(random.choices(letters, k=10))
    new =f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'
    
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {'filename':path}
    

    


