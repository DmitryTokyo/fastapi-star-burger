from backend.db.db_init import Base
from sqlalchemy import Column, Float, Integer, String


class Restaurant(Base):
    """Restaurant model"""

    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True, index=True)
    title = Column('Restaurant title', String(100))
    address = Column(String(100))
    contact_phone = Column('Contact phone', String(50))
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)

    def __str__(self) -> str:
        return self.title
