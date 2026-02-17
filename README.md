# MiniRetail API

A minimal retail API and UI for managing products and a shopping cart.

## Features

- **Products Management**: Create, Read, Update, Delete products
- **Shopping Cart**: Add items, list cart with totals, remove items
- **SQLite Database**: Local database storage
- **REST API**: FastAPI-based REST API
- **Web UI**: Simple HTML/JavaScript interface
- **Automated Tests**: Comprehensive test suite

## Tech Stack

- Python 3.10+
- FastAPI
- SQLite
- Pytest
- Vanilla JavaScript

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Start the API Server

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`
API documentation: `http://localhost:8000/docs`

### Access the Web UI

Open `frontend/index.html` in a browser or serve it with:
```bash
python -m http.server 8080 --directory frontend
```

Then visit: `http://localhost:8080/index.html`

## API Endpoints

### Products
- `POST /products` - Create a product
- `GET /products` - List all products
- `GET /products/{id}` - Get a specific product
- `PUT /products/{id}` - Update a product
- `DELETE /products/{id}` - Delete a product

### Shopping Cart
- `POST /cart/add` - Add item to cart (body: `{product_id: int, qty: int}`)
- `GET /cart` - Get cart items with total
- `DELETE /cart/{id}` - Remove item from cart

## Running Tests

```bash
pytest tests/test_retail.py -v
```

## Database Schema

### products
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT NOT NULL)
- `price` (REAL NOT NULL)
- `stock` (INTEGER NOT NULL)
- `created_at` (TIMESTAMP)

### cart_items
- `id` (INTEGER PRIMARY KEY)
- `product_id` (INTEGER FOREIGN KEY)
- `qty` (INTEGER NOT NULL)
- `added_at` (TIMESTAMP)

## Project Structure

```
MiniRetail/
├── backend/
│   ├── __init__.py
│   ├── main.py          # FastAPI app and routes
│   ├── database.py      # SQLite connection
│   ├── models.py        # Data models
│   ├── schemas.py       # Pydantic schemas
│   └── crud.py          # Database operations
├── frontend/
│   └── index.html       # Web UI
├── tests/
│   └── test_retail.py   # Test suite
├── requirements.txt
└── README.md
```

## Out of Scope

This is a minimal demo application. The following are intentionally excluded:
- Authentication/Authorization
- Payments
- Coupons/Discounts
- Pagination
- User accounts
- Async database operations
