from sqlalchemy.orm import relationship

from backend.db.db_init import Base
from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey, UniqueConstraint


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


class RestaurantMenuItem(Base):
    __tablename__ = 'restaurant_menu_item'
    _table_args__ = (
        UniqueConstraint('restaurant_id', 'product_id'),
    )

    id = Column(Integer, primary_key=True, index=True)
    available = Column('Product available in menu', Boolean, default=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', backref='menu_items')
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship('Restaurant', backref='menu_items')

    def __str__(self) -> str:
        return f'{self.restaurant.title} - {self.product.title}'
