from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  DATABASE_URL: str
  timezone: str = 'Asia/Kuala_Lumpur'

  model_config = SettingsConfigDict(env_file='../.env', extra='ignore', case_sensitive=True)

settings = Settings()