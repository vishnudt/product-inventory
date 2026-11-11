from sqlalchemy import Column, String, Integer
from database import Base

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)