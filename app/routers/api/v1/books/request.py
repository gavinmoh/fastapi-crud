from pydantic import BaseModel
from typing import Optional

class BookCreateRequest(BaseModel):
  title: str
  description: Optional[str] = None

class BookUpdateRequest(BaseModel):
  title: Optional[str] = None
  description: Optional[str] = None