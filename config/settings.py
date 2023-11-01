from pydantic import BaseSettings


class Settings(BaseSettings):
  DATABASE_URL: str

  class Config:
    case_sensitive = True
    env_file = '../.env'
    env_file_encoding = 'utf-8'

settings = Settings()