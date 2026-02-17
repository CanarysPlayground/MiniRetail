# MiniRetail — Requirements & Architecture (Source of Truth)

## Business Goal
Provide a minimal retail API and UI for demo purposes: manage products and a simple shopping cart. No user accounts, no payments.

## In-Scope (MVP)
- Products: Create, Read, Update, Delete
- Cart: Add item, List cart with totals, Remove item
- Local SQLite database
- Minimal static UI (single HTML) calling the API via fetch
- Automated tests using pytest + FastAPI TestClient
- Background task demo: purge all cart items every 30 seconds (for showcase)

## Out of Scope
- Authentication, authorization
- Payments, coupons, discounts, pagination, users
- External APIs, async DB

## Non-Functional
- Python 3.10+
- FastAPI
- SQLite (single file `retail.db`)
- Deterministic, minimal code; synchronous only
- Keep code simple, readable, and organized

## Data Model
### Table: products
- id (int, primary key)
- name (string, required)
- price (float, >= 0)
- stock (int, >= 0)
- created_at (datetime)

### Table: cart_items
- id (int, primary key)
- product_id (int, fk → products.id)
- qty (int, > 0)
- added_at (datetime)

## API Contract
### /products
- POST /products      → create product
- GET  /products      → list products
- GET  /products/{id} → get product
- PUT  /products/{id} → update product
- DELETE /products/{id} → delete product

### /cart
- POST   /cart/add           → body { product_id:int, qty:int }
- GET    /cart               → list items (+ embedded product info) + total
- DELETE /cart/{id}          → remove a cart item by id

## Architecture & Design
- **Backend (FastAPI)**: `backend/`
  - `database.py` — SQLite init/connection helpers
  - `models.py` — SQL DDL or ORM definitions
  - `schemas.py` — Pydantic request/response models
  - `crud.py` — DB logic for products & cart
  - `main.py` — FastAPI app, routes, dependency wiring
- **Frontend**: `frontend/index.html` — vanilla HTML + JS (fetch)
- **Tests**: `tests/test_retail.py` — pytest + TestClient
- **Background Agent**: `backend/cleanup_cart_items.py`
  - Runs independently; every 30s deletes all rows in `cart_items`
  - Synchronous script; no scheduling framework

## Typical Flows
- Add product → List products → Update product → Delete product
- Add to cart → Get cart (recalculate total) → Remove cart item
- Background: every 30s truncates cart_items for demo reset



## Constraints
- No auth, no payments/coupons/pagination/users
- Synchronous only; no async DB
- Keep files exactly in the prescribed paths
- Deterministic outputs; minimalism preferred
minifeed/
│
├── instructions/
│   └── standard.instructions.md
│
├── prompts/
│   ├── api.prompt.md
│   ├── ui.prompt.md
│   └── test.prompt.md
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── crud.py
│
├── frontend/
│   └── index.html
│
├── tests/
│   └── test_posts.py