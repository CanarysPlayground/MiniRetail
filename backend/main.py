from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Product, CartItem
from .schemas import Product, ProductCreate, ProductUpdate, CartItem, CartItemCreate
from .crud import (
    get_products, get_product, create_product, update_product, delete_product,
    get_cart, add_to_cart, remove_cart_item
)

Base.metadata.create_all(bind=engine)
app = FastAPI()

# Serve frontend static files
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Products
@app.get("/api/products", response_model=list[Product])
def list_products(db: Session = Depends(get_db)):
    return get_products(db)

@app.post("/api/products", response_model=Product)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@app.put("/api/products/{product_id}", response_model=Product)
def edit_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = update_product(db, product_id, product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.delete("/api/products/{product_id}", response_model=Product)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Cart
@app.get("/api/cart", response_model=list[CartItem])
def list_cart(db: Session = Depends(get_db)):
    return get_cart(db)

@app.post("/api/cart", response_model=CartItem)
def add_cart_item(item: CartItemCreate, db: Session = Depends(get_db)):
    cart_item = add_to_cart(db, item)
    if not cart_item:
        raise HTTPException(status_code=400, detail="Invalid product or insufficient stock")
    return cart_item

@app.delete("/api/cart/{product_id}", response_model=CartItem)
def remove_cart_item_route(product_id: int, db: Session = Depends(get_db)):
    cart_item = remove_cart_item(db, product_id)
    if not cart_item:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return cart_item
