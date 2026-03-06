# FastAPI Assignment 1

This assignment demonstrates building REST APIs using FastAPI.

## Implemented Endpoints

1. **GET /products**
   - Returns all products with total count.

2. **GET /products/category/{category_name}**
   - Filters products based on category.

3. **GET /products/instock**
   - Shows only products that are currently available.

4. **GET /store/summary**
   - Returns store statistics such as total products, in-stock count, and categories.

5. **GET /products/search/{keyword}**
   - Searches products by name (case-insensitive).

6. **GET /products/deals**
   - Returns cheapest product (best deal) and most expensive product (premium pick).

## Files Included

- `main.py` → FastAPI application
- Output screenshots for each endpoint
- `README.md` → Documentation for the assignment

## How to Run

```bash
uvicorn main:app --reload