from sqlalchemy import Column, Integer, String, Text

from backend.db.db_init import Base


class Banner(Base):
    """Banner model."""

    __tablename__ = 'banner'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), index=True)
    description = Column(Text, nullable=True)
    banner_order = Column(Integer, default=0, index=True)
    image_file = Column(Text, nullable=False)

    def __str__(self) -> str:
        return self.title
