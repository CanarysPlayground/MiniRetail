from sqlalchemy.orm import Session
from .models import Product, CartItem
from .schemas import ProductCreate, ProductUpdate, CartItemCreate

# Product CRUD

def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product(db, product_id)
    if db_product:
        for field, value in product.dict().items():
            setattr(db_product, field, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# Cart

def get_cart(db: Session):
    return db.query(CartItem).all()

def add_to_cart(db: Session, item: CartItemCreate):
    product = get_product(db, item.product_id)
    if not product or product.stock < item.qty:
        return None
    db_cart_item = db.query(CartItem).filter(CartItem.product_id == item.product_id).first()
    if db_cart_item:
        db_cart_item.qty += item.qty
    else:
        db_cart_item = CartItem(product_id=item.product_id, name=product.name, price=product.price, qty=item.qty)
        db.add(db_cart_item)
    product.stock -= item.qty
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

def remove_cart_item(db: Session, product_id: int):
    cart_item = db.query(CartItem).filter(CartItem.product_id == product_id).first()
    if cart_item:
        product = get_product(db, product_id)
        if product:
            product.stock += cart_item.qty
        db.delete(cart_item)
        db.commit()
    return cart_item
