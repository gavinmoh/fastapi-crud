# from pydantic import BaseModel
from sqlalchemy import Column, String
from .base import SQLBase
from sqlalchemy import Column
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql
from sqlalchemy import TIMESTAMP


class Book(SQLBase):
  __tablename__ = 'books'
  
  id = Column(postgresql.UUID, primary_key=True, server_default=func.gen_random_uuid())
  title = Column(String, default=None, nullable=False)
  description = Column(String, default=None, nullable=True)
  created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
  updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)

# class Book(BaseModel):
#   id: Optional[uuid.UUID] = None
#   title: str
#   description: Optional[str] = None
#   created_at: Optional[datetime.datetime] = None
#   updated_at: Optional[datetime.datetime] = None

#   class Config:
#     orm_mode = True
