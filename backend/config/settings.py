import os
import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.environ.get('SECRET_KEY', default=secrets.token_urlsafe(32))
    DB_URL: str = 'postgresql://andimeon:565651db@localhost:5432/star_burger_fast'
    PROJECT_NAME: str = 'Fast api star burger version'

    class Config:
        case_sensitive = True


settings = Settings()
