from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    stock: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class CartItemBase(BaseModel):
    product_id: int
    qty: int

class CartItemCreate(CartItemBase):
    pass

class CartItem(CartItemBase):
    name: str
    price: float
    class Config:
        orm_mode = True
