---
name: API-prompt
description: This prompt is used to generate the backend API code for a mini retail application using FastAPI and SQLite. The API will include endpoints for managing products and a shopping cart, following specific requirements and architecture guidelines.
model: Claude Opus 4.6 (fast mode) (Preview)
---
Using the standard instructions:

Task:
Build the backend API for MiniRetail.

Requirements:
- FastAPI + SQLite retail.db
- Implement:
  - products CRUD
  - cart add/list/remove
- Separate into:
  backend/database.py
  backend/models.py
  backend/schemas.py
  backend/crud.py
  backend/main.py

Return:
Complete backend code for the above files only.