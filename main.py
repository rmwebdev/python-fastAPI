from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


# @app.get('/')
# def index():
#     return {'data': 'blogs list'}

@app.get('/blog')
def index(limit=10, published:bool=True, sort:Optional[str]=None):
    if published:
        return {'data': f'{limit} published blogs list from db'}
    else:
        return {'data': f'{limit} blogs list from db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'blogs unpublished list'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}


# @app.get('/blog/{id}/comments')
# def comments(id:int):
#     return {'data': {'1', '2', '3'}}

@app.get('/blog/{id}/comments')
def comments(id:int, limit=10):
    return {'data': {'1', '2', '3'}}


class BlogModel(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

@app.post('/blog/')
def createBlog(blog: BlogModel):
    return {'data': "oks"}