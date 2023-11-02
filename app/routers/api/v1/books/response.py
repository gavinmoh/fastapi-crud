from pydantic import BaseModel
from typing import Optional
import uuid
import datetime

class BookResponse(BaseModel):
  id: uuid.UUID
  title: str
  description: Optional[str] = None
  created_at: datetime.datetime
  updated_at: datetime.datetime

  class Config:
    orm_mode = True