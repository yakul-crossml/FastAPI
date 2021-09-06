from fastapi import FastAPI,APIRouter, Depends, status, HTTPException
from Blog import schemas, database, models,oaut2
from typing import List
from sqlalchemy.orm import Session
from Blog.repository import blog

get_db = database.get_db

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User=Depends(oaut2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User=Depends(oaut2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destory(id, db: Session = Depends(get_db), current_user: schemas.User=Depends(oaut2.get_current_user)):
    return blog.destory(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User=Depends(oaut2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, tags=['Blogs'])
def show(id, db: Session = Depends(get_db), current_user: schemas.User=Depends(oaut2.get_current_user)):
    return blog.show(id, db)
