The UI is now served via FastAPI.
 You can access it at http://127.0.0.1:8000/ in your browser.

 for API
 http://127.0.0.1:8000/api/products
http://127.0.0.1:8000/api/cart

To run the API server:

Install dependencies: 
pip install fastapi sqlalchemy pydantic uvicorn
Start the server:
uvicorn backend.main:app --reload