from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  DATABASE_URL: str

  model_config = SettingsConfigDict(env_file='../.env', extra='ignore', case_sensitive=True)

settings = Settings()