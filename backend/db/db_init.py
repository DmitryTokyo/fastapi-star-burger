from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from backend.config.settings import settings

engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
