from pydantic import BaseModel, field_serializer
import uuid
import datetime
from app.utils.timezone import utc_to_local

class ResponseBase(BaseModel):
  id: uuid.UUID
  created_at: datetime.datetime
  updated_at: datetime.datetime

  @field_serializer('created_at')
  def local_created_at(self, _attr, _info):
    return utc_to_local(self.created_at)
  
  @field_serializer('updated_at')
  def local_updated_at(self, _attr, _info):
    return utc_to_local(self.updated_at)
  
  class Config:
    orm_mode = True