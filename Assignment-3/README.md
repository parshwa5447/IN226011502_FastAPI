# FastAPI Assignment 3

## 📌 Project Overview

This assignment demonstrates **CRUD operations using FastAPI**.
The API simulates a small **E-commerce product management system** where products can be added, updated, deleted, and analyzed.

The assignment includes:

* POST requests (create products)
* GET requests (fetch products)
* PUT requests (update products)
* DELETE requests (remove products)
* Business logic endpoints like **inventory audit** and **category discount**

---

# ⚙️ Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

---

# 🚀 How to Run the Project

### Install dependencies

```bash
pip install fastapi uvicorn
```

### Run the server

```bash
uvicorn main:app --reload
```

### Open API documentation

```
http://127.0.0.1:8000/docs
```

Swagger UI will appear where you can test all endpoints.

---

# 📂 Project Structure

```
IN226011502_FASTAPI
│
├── Assignment-1
│
├── Assignment-2
│
└── Assignment-3
    ├── main.py
    ├── README.md
    └── Output (API screenshots)
```

---

# 🔗 Implemented API Endpoints

## 1️⃣ Add New Products

```
POST /products
```

Adds a new product with auto-generated ID.

Example request:

```json
{
 "name": "Laptop Stand",
 "price": 1299,
 "category": "Electronics",
 "in_stock": true
}
```

Response:

```json
{
 "message": "Product added",
 "product": {
   "id": 5,
   "name": "Laptop Stand",
   "price": 1299,
   "category": "Electronics",
   "in_stock": true
 }
}
```

Duplicate product names return **400 Bad Request**.

---

## 2️⃣ Update Product (Restock / Price Change)

```
PUT /products/{product_id}
```

Example:

```
/products/3?in_stock=true
/products/3?price=699
/products/3?price=649&in_stock=true
```

Used for restocking products and updating prices.

---

## 3️⃣ Delete Product

```
DELETE /products/{product_id}
```

Example:

```
DELETE /products/4
```

Response:

```json
{
 "message": "Product 'Pen Set' deleted"
}
```

Deleting a missing product returns **404 Not Found**.

---

## 4️⃣ Product CRUD Workflow

Complete lifecycle example:

1. Add product using POST
2. View product using GET
3. Update price using PUT
4. Delete product using DELETE

This simulates a real **product launch and cancellation workflow**.

---

## 5️⃣ Product Audit Endpoint

```
GET /products/audit
```

Returns store inventory summary:

```json
{
 "total_products": 4,
 "in_stock_count": 3,
 "out_of_stock_names": ["USB Hub"],
 "total_stock_value": 6470,
 "most_expensive": {
   "name": "USB Hub",
   "price": 799
 }
}
```

This helps store managers analyze inventory.

---

# ⭐ Bonus Feature – Category Discount

```
PUT /products/discount
```

Applies a percentage discount to all products in a category.

Example:

```
/products/discount?category=Electronics&discount_percent=10
```

Response:

```json
{
 "updated_products": [
   {"name":"Wireless Mouse","new_price":449},
   {"name":"USB Hub","new_price":719}
 ],
 "count": 2
}
```

---

# 📸 Output Screenshots

Screenshots of API responses are included inside the **Output folder** for verification.

---

# 👨‍💻 Author

**Parshwa Desai**

FastAPI Internship Assignment
Innovatics Research Labs
