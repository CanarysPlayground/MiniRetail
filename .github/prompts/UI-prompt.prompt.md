---
name: UI-prompt
description: This prompt is used to generate a minimal frontend UI for the MiniRetail project. The UI will allow users to add products, list products with edit/delete options.
model: Claude Opus 4.6 (fast mode) (Preview)
---
Using the standard instructions:

Task:
Create the minimal frontend UI.

Requirements:
- Single file: frontend/index.html
- Plain HTML + JavaScript (fetch)
- Features:
  - Form: add product (name, price, stock)
  - List products with edit/delete
  - Form: add to cart (product_id, qty)
  - List cart items with total; remove cart item
- No CSS frameworks

Return:
frontend/index.html only.