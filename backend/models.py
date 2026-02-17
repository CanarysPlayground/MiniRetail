from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer)

class CartItem(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    name = Column(String)
    price = Column(Float)
    qty = Column(Integer)
