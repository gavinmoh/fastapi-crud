from app.models.response import ResponseBase
from typing import Optional

class BookResponse(ResponseBase):
  title: str
  description: Optional[str] = None