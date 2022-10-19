import os
import secrets

from fastapi.staticfiles import StaticFiles
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Fast api star burger version'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    API_V1_STR: str = '/api/v1'
    SECRET_KEY: str = os.environ.get('SECRET_KEY', default=secrets.token_urlsafe(32))

    DB_URL: str = 'postgresql+asyncpg://andimeon:565651db@localhost:5432/star_burger_fast'
    PROJECT_NAME: str = 'Fast api star burger version'

    STATIC_ROOT = StaticFiles(directory=os.path.join(BASE_DIR, "static"))
    MEDIA_ROOT: str = './backend/media/'

    class Config:
        case_sensitive = True


settings = Settings()
