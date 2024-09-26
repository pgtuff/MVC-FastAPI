# backend/app/models.py

from sqlalchemy import Column, Integer, String, Float
from .database import Base

# Define the "Item" model/table
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
