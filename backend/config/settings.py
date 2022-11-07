import os
import secrets

from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Fast api star burger version'
    BACKEND_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ROOT_DIR = os.path.dirname(BACKEND_DIR)
    API_V1_STR: str = '/api'
    SECRET_KEY: str = os.environ.get('SECRET_KEY', default=secrets.token_urlsafe(32))

    DB_URL: str = 'postgresql+asyncpg://andimeon:565651db@localhost:5432/star_burger_fast'
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        'http://localhost',
        'http://localhost:8000',
    ]

    MEDIA_ROOT: str = f'{BACKEND_DIR}/media/'

    class Config:
        case_sensitive = True


settings = Settings()
