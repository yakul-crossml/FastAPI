from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    body: str
    publish: Optional[bool]


app = FastAPI()


@app.post('/blog')
def create_blog(blog: Item):
    return {'data': f"this is my first blog who name is {blog.title}"}


@app.get('/blogs')
def index(limit, published: bool, sort: Optional[str] = None):
    return published, sort
    return {"data": {limit: "Yakul"}}


@app.get('/about')
def about():
    return{'data': 'About Page'}


@app.get('/blogs/{id}')
def show(id: int):
    return{'data': id}


@app.get('/blogs/{id}/comments')
def show(id):
    return{'data': {id: {'comment1', 'comment2'}}}
