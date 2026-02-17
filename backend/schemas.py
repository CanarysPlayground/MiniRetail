from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    price: float = Field(ge=0)
    stock: int = Field(ge=0)


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(None, ge=0)
    stock: Optional[int] = Field(None, ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    created_at: datetime


class CartItemAdd(BaseModel):
    product_id: int
    qty: int = Field(gt=0)


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    qty: int
    added_at: datetime
    product_name: str
    product_price: float


class CartResponse(BaseModel):
    items: list[CartItemResponse]
    total: float
