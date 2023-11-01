from typing import Optional
from fastapi import APIRouter, HTTPException, Path, Depends
from config.database import get_session
from sqlalchemy.orm import Session
from app.models.book import Book, get_books
from pydantic import BaseModel
from app.exceptions.resource_not_found import ResourceNotFoundException
router = APIRouter()

class BookCreateRequest(BaseModel):
  title: str
  description: Optional[str] = None

class BookUpdateRequest(BaseModel):
  title: Optional[str] = None
  description: Optional[str] = None

def find_book(id: str, session: Session):
  book = session.get(Book, id)
  if book is None:
    raise ResourceNotFoundException()
  return book

@router.get('/')
async def list_books(session:Session=Depends(get_session), offset:int=0, limit:int=20):
  books = session.query(Book).offset(offset).limit(limit).all()
  return { "books": books }

@router.post('/', status_code=201)
async def create_book(request:BookCreateRequest, session:Session=Depends(get_session)):
  book = Book(**request.dict())
  session.add(book)
  session.commit()
  session.refresh(book)
  return { "book": book}

@router.get('/{id}')
async def show_book(id:str, session:Session=Depends(get_session)):
  book = find_book(id, session)
  return { "book": book}

@router.put('/{id}')
async def update_book(id:str, request: BookUpdateRequest, session:Session=Depends(get_session)):
  book = find_book(id, session)
  for key, value in request.dict(exclude_unset=True).items():
    setattr(book, key, value)
  session.commit()
  session.refresh(book)
  return { "book": book}

@router.delete('/{id}', status_code=204)
async def remove_book(id:str, session:Session=Depends(get_session)):
  book = find_book(id, session)
  session.delete(book)
  session.commit()