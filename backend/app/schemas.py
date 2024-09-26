# backend/app/schemas.py

from pydantic import BaseModel

# Base schema for Item
class ItemBase(BaseModel):
    name: str
    description: str = None
    price: float

# Schema for creating an Item
class ItemCreate(ItemBase):
    pass

# Schema for reading an Item (with id)
class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True
