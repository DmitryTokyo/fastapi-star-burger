from typing import Generator

from backend.db.db_init import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
