import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.database import init_db
import os


@pytest.fixture(autouse=True)
def setup_test_db():
    if os.path.exists("retail.db"):
        os.remove("retail.db")
    init_db()
    yield
    if os.path.exists("retail.db"):
        os.remove("retail.db")


client = TestClient(app)


def test_create_product():
    response = client.post("/products", json={
        "name": "Test Product",
        "price": 10.99,
        "stock": 100
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 10.99
    assert data["stock"] == 100
    assert "id" in data
    assert "created_at" in data


def test_list_products():
    client.post("/products", json={"name": "Product 1", "price": 10.0, "stock": 10})
    client.post("/products", json={"name": "Product 2", "price": 20.0, "stock": 20})
    
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_get_product():
    create_response = client.post("/products", json={
        "name": "Test Product",
        "price": 15.99,
        "stock": 50
    })
    product_id = create_response.json()["id"]
    
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 15.99


def test_get_product_not_found():
    response = client.get("/products/999")
    assert response.status_code == 404


def test_update_product():
    create_response = client.post("/products", json={
        "name": "Old Name",
        "price": 10.0,
        "stock": 10
    })
    product_id = create_response.json()["id"]
    
    response = client.put(f"/products/{product_id}", json={
        "name": "New Name",
        "price": 15.0
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "New Name"
    assert data["price"] == 15.0
    assert data["stock"] == 10


def test_update_product_not_found():
    response = client.put("/products/999", json={"name": "New Name"})
    assert response.status_code == 404


def test_delete_product():
    create_response = client.post("/products", json={
        "name": "To Delete",
        "price": 10.0,
        "stock": 10
    })
    product_id = create_response.json()["id"]
    
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 204
    
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404


def test_delete_product_not_found():
    response = client.delete("/products/999")
    assert response.status_code == 404


def test_add_to_cart():
    product_response = client.post("/products", json={
        "name": "Cart Product",
        "price": 25.0,
        "stock": 10
    })
    product_id = product_response.json()["id"]
    
    response = client.post("/cart/add", json={
        "product_id": product_id,
        "qty": 2
    })
    assert response.status_code == 201
    data = response.json()
    assert data["product_id"] == product_id
    assert data["qty"] == 2
    assert data["product_name"] == "Cart Product"
    assert data["product_price"] == 25.0


def test_add_to_cart_product_not_found():
    response = client.post("/cart/add", json={
        "product_id": 999,
        "qty": 1
    })
    assert response.status_code == 404


def test_get_cart():
    product1 = client.post("/products", json={"name": "P1", "price": 10.0, "stock": 10}).json()
    product2 = client.post("/products", json={"name": "P2", "price": 20.0, "stock": 10}).json()
    
    client.post("/cart/add", json={"product_id": product1["id"], "qty": 2})
    client.post("/cart/add", json={"product_id": product2["id"], "qty": 1})
    
    response = client.get("/cart")
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 2
    assert data["total"] == 40.0


def test_delete_cart_item():
    product = client.post("/products", json={"name": "P1", "price": 10.0, "stock": 10}).json()
    cart_item = client.post("/cart/add", json={"product_id": product["id"], "qty": 1}).json()
    
    response = client.delete(f"/cart/{cart_item['id']}")
    assert response.status_code == 204
    
    cart_response = client.get("/cart")
    assert len(cart_response.json()["items"]) == 0


def test_delete_cart_item_not_found():
    response = client.delete("/cart/999")
    assert response.status_code == 404
