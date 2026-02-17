from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.database import init_db
from backend import crud
from backend.schemas import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    CartItemAdd,
    CartItemResponse,
    CartResponse
)

app = FastAPI(title="MiniRetail API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    init_db()


@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):
    return crud.create_product(product)


@app.get("/products", response_model=list[ProductResponse])
def list_products():
    return crud.get_products()


@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    product = crud.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate):
    updated = crud.update_product(product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    deleted = crud.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")


@app.post("/cart/add", response_model=CartItemResponse, status_code=201)
def add_to_cart(cart_item: CartItemAdd):
    result = crud.add_to_cart(cart_item)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result


@app.get("/cart", response_model=CartResponse)
def get_cart():
    return crud.get_cart()


@app.delete("/cart/{cart_item_id}", status_code=204)
def delete_cart_item(cart_item_id: int):
    deleted = crud.delete_cart_item(cart_item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cart item not found")
