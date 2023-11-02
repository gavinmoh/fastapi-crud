from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import settings

engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
  with SessionLocal() as session:
    yield session
