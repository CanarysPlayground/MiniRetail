from datetime import datetime


class Product:
    def __init__(self, id, name, price, stock, created_at):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.created_at = created_at


class CartItem:
    def __init__(self, id, product_id, qty, added_at):
        self.id = id
        self.product_id = product_id
        self.qty = qty
        self.added_at = added_at
