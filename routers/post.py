from fastapi import APIRouter, Depends
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_post

router = APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('')
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)

@router.get('')
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)
