from backend.db.db_init import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship


class ProductCategory(Base):
    """Product category model"""

    __tablename__ = 'products_category'

    id = Column(Integer, primary_key=True, index=True)
    title = Column('Product category title', String(100))

    def __str__(self) -> str:
        return self.title


class Product(Base):
    """Product model"""

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    title = Column('Product title', String(100))
    price = Column('Product price', Numeric(precision=8, scale=2, asdecimal=True))
    image_url = Column('Product image url', String(100))
    special_status = Column('Special status', Boolean, default=False, index=True)
    ingredients = Column(String(200), nullable=True)
    product_category_id = Column(Integer, ForeignKey('products_category.id'))
    product_category = relationship('ProductCategory', backref='products')

    def __str__(self) -> str:
        return self.title
