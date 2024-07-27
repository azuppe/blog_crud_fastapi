from fastapi import FastAPI
from database import models
from database import database
from routers import post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import  CORSMiddleware

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)
app.include_router(post.router)
app.mount('/images', StaticFiles(directory='images'), name='images')

origins=['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods =['*'],
    allow_headers=['*'],
)