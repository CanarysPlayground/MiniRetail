---
description: Describe when these instructions should be loaded
applyTo: '**/*.py, **/*.html'
---
You are an expert Python FastAPI developer.

GLOBAL RULES (MANDATORY)
1. Python 3.10+, FastAPI, SQLite (file: retail.db)
2. Follow exact folder structure under /miniretail
3. Do NOT add authentication, payments, coupons, pagination, or users
4. Keep logic simple and readable
5. Use synchronous code only (no async DB)
6. Every resource exposes standard CRUD where applicable
7. Use Pydantic schemas for request/response
8. Implement only the listed endpoints
9. Do not introduce new folders or files beyond the structure
10. Produce deterministic, minimal code; no explanations unless asked

DATABASE TABLES
- products(id pk, name str, price float, stock int, created_at dt)
- cart_items(id pk, product_id fk, qty int, added_at dt)

API ROUTES
- /products: POST, GET, GET/{id}, PUT/{id}, DELETE/{id}
- /cart: POST /cart/add, GET /cart, DELETE /cart/{id}

OUTPUT
- Write code only into:
  - backend/database.py
  - backend/models.py
  - backend/schemas.py
  - backend/crud.py
  - backend/main.py
  - frontend/index.html
  - tests/test_retail.py