from backend.database import get_db
from backend.schemas import ProductCreate, ProductUpdate, CartItemAdd
from datetime import datetime


def create_product(product: ProductCreate):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
            (product.name, product.price, product.stock)
        )
        product_id = cursor.lastrowid
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        return dict(row)


def get_products():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products ORDER BY created_at DESC")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]


def get_product(product_id: int):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        return dict(row) if row else None


def update_product(product_id: int, product: ProductUpdate):
    with get_db() as conn:
        cursor = conn.cursor()
        
        existing = get_product(product_id)
        if not existing:
            return None
        
        updates = []
        params = []
        
        if product.name is not None:
            updates.append("name = ?")
            params.append(product.name)
        if product.price is not None:
            updates.append("price = ?")
            params.append(product.price)
        if product.stock is not None:
            updates.append("stock = ?")
            params.append(product.stock)
        
        if updates:
            params.append(product_id)
            cursor.execute(
                f"UPDATE products SET {', '.join(updates)} WHERE id = ?",
                params
            )
        
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        return dict(row)


def delete_product(product_id: int):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        if not row:
            return False
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        return True


def add_to_cart(cart_item: CartItemAdd):
    with get_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM products WHERE id = ?", (cart_item.product_id,))
        product = cursor.fetchone()
        if not product:
            return None
        
        cursor.execute(
            "INSERT INTO cart_items (product_id, qty) VALUES (?, ?)",
            (cart_item.product_id, cart_item.qty)
        )
        cart_item_id = cursor.lastrowid
        
        cursor.execute("""
            SELECT ci.*, p.name as product_name, p.price as product_price
            FROM cart_items ci
            JOIN products p ON ci.product_id = p.id
            WHERE ci.id = ?
        """, (cart_item_id,))
        row = cursor.fetchone()
        return dict(row)


def get_cart():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT ci.*, p.name as product_name, p.price as product_price
            FROM cart_items ci
            JOIN products p ON ci.product_id = p.id
            ORDER BY ci.added_at DESC
        """)
        rows = cursor.fetchall()
        items = [dict(row) for row in rows]
        total = sum(item['product_price'] * item['qty'] for item in items)
        return {'items': items, 'total': total}


def delete_cart_item(cart_item_id: int):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cart_items WHERE id = ?", (cart_item_id,))
        row = cursor.fetchone()
        if not row:
            return False
        cursor.execute("DELETE FROM cart_items WHERE id = ?", (cart_item_id,))
        return True
