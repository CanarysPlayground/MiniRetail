---
name: tests-prompt
description: This prompt is used to generate test cases for the MiniRetail API using pytest and FastAPI's TestClient. The tests will cover creating, listing, updating, and deleting products, as well as adding items to the cart, retrieving the cart with total validation, and removing cart items.
---
You are a test automation agent.

Task:
Write tests for the MiniRetail API.

Rules:
- Use pytest
- Use FastAPI TestClient
- Cover:
  - create product
  - list products
  - update product
  - delete product
  - add to cart
  - get cart (validate total)
  - remove cart item

Output:
tests/test_retail.py