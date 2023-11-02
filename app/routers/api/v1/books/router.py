import math
from fastapi import APIRouter, Depends, Response
from config.database import get_session
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from app.models.book import Book
from app.exceptions.resource_not_found import ResourceNotFoundException
from .request import BookCreateRequest, BookUpdateRequest
from .response import BookResponse
from app.utils.paginator import paginate, set_pagination_headers
from app.utils.sorter import sort

router = APIRouter()

def find_book(id: str, session: Session):
  book = session.get(Book, id)
  if book is None:
    raise ResourceNotFoundException()
  return book

@router.get('/', response_model=list[BookResponse])
async def list_books(response: Response, session:Session=Depends(get_session), query:str=None, sort_by:str=None, sort_order:str=None, page:int=1, items:int=20):
  books = session.query(Book)
  books = sort(books, sort_by, sort_order)
  if query:
    books = books.filter(Book.title.ilike(f'%{query}%'))
  count, books, pages = paginate(books, page, items)
  set_pagination_headers(response, count, pages, page, items)
  return books

@router.post('/', status_code=201, response_model=BookResponse)
async def create_book(request:BookCreateRequest, session:Session=Depends(get_session)):
  book = Book(**request.model_dump())
  session.add(book)
  session.commit()
  session.refresh(book)
  return book

@router.get('/{id}', response_model=BookResponse)
async def show_book(id:str, session:Session=Depends(get_session)):
  book = find_book(id, session)
  return book

@router.put('/{id}', response_model=BookResponse)
async def update_book(id:str, request: BookUpdateRequest, session:Session=Depends(get_session)):
  book = find_book(id, session)
  for key, value in request.model_dump(exclude_unset=True).items():
    setattr(book, key, value)
  session.commit()
  session.refresh(book)
  return book

@router.delete('/{id}', status_code=204)
async def remove_book(id:str, session:Session=Depends(get_session)):
  book = find_book(id, session)
  session.delete(book)
  session.commit()