from sqlmodel import Field, SQLModel
from sqlalchemy import Column
from sqlalchemy.sql import func
from typing import Optional
import datetime
import uuid

class Book(SQLModel, table=True):
  __tablename__ = 'books'
  
  id: Optional[uuid.UUID] = Field(sa_column=Column(primary_key=True, server_default=func.gen_random_uuid()))
  title: str = Field(default=None, nullable=False)
  description: Optional[str] = Field(default=None, nullable=True)
  created_at: Optional[datetime.datetime] = Field(sa_column=Column(server_default=func.now(), nullable=False))
  updated_at: Optional[datetime.datetime] = Field(sa_column=Column(server_default=func.now(), onupdate=func.now(), nullable=False))

def get_books(db, offset=0, limit=100):
  books = db.query(Book).offset(offset).limit(limit).all()
  return books

