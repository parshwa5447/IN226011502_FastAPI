# FastAPI Assignment 4 – Cart System

## 📌 Project Overview

This project implements a **shopping cart system using FastAPI**.
Customers can add products to a cart, update quantities, remove items, and complete checkout.
The API also manages orders created after checkout.

The assignment demonstrates:

* REST API design
* Cart management logic
* Error handling
* Order creation and tracking

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

Swagger UI allows testing all endpoints interactively.

---

# 📂 Project Structure

```
IN226011502_FASTAPI
│
├── Assignment-1
│
├── Assignment-2
│
├── Assignment-3
│
└── Assignment-4
    ├── main.py
    ├── README.md
    └── Output (API screenshots)
```

---

# 🛒 Cart API Endpoints

## 1️⃣ Add Item to Cart

```
POST /cart/add
```

Example:

```
/cart/add?product_id=1&quantity=2
```

Response example:

```json
{
  "message": "Added to cart",
  "cart_item": {
    "product_id": 1,
    "product_name": "Wireless Mouse",
    "quantity": 2,
    "unit_price": 499,
    "subtotal": 998
  }
}
```

If the product already exists in the cart, the quantity is updated instead of creating a duplicate entry.

---

## 2️⃣ View Cart

```
GET /cart
```

Example response:

```json
{
  "items": [
    {
      "product_id": 1,
      "product_name": "Wireless Mouse",
      "quantity": 2,
      "unit_price": 499,
      "subtotal": 998
    },
    {
      "product_id": 2,
      "product_name": "Notebook",
      "quantity": 1,
      "unit_price": 99,
      "subtotal": 99
    }
  ],
  "item_count": 2,
  "grand_total": 1097
}
```

---

## 3️⃣ Remove Item from Cart

```
DELETE /cart/{product_id}
```

Example:

```
DELETE /cart/2
```

Response:

```json
{
  "message": "Notebook removed from cart"
}
```

---

## 4️⃣ Checkout

```
POST /cart/checkout
```

Request body example:

```json
{
  "customer_name": "Parshwa",
  "delivery_address": "Pune Maharashtra India"
}
```

Example response:

```json
{
  "message": "Checkout successful",
  "orders_placed": [
    {
      "order_id": 1,
      "customer_name": "Parshwa",
      "product": "Wireless Mouse",
      "quantity": 3,
      "subtotal": 1497,
      "delivery_address": "Pune Maharashtra India"
    }
  ],
  "grand_total": 1497
}
```

After checkout, the cart becomes empty.

---

# 📦 Orders Endpoint

## View All Orders

```
GET /orders
```

Example response:

```json
{
  "orders": [
    {
      "order_id": 1,
      "customer_name": "Customer 1",
      "product": "Wireless Mouse",
      "quantity": 1,
      "subtotal": 499
    }
  ],
  "total_orders": 1
}
```

---

# ❌ Error Handling

### Product Not Found

```
404 Not Found
```

```json
{
  "detail": "Product not found"
}
```

### Product Out of Stock

```
400 Bad Request
```

```json
{
  "detail": "USB Hub is out of stock"
}
```

### Checkout with Empty Cart

```
400 Bad Request
```

```json
{
  "detail": "CART_EMPTY"
}
```

---

# ⭐ Features Implemented

* Add products to cart
* Update quantity automatically
* Remove items from cart
* Cart total calculation
* Checkout system
* Order history
* Error handling for invalid operations

---

# 📸 Output Screenshots

All API responses are captured and stored in the **Output folder** for verification.

---

# 👨‍💻 Author

**Parshwa Desai**

FastAPI Internship Assignment
Innovatics Research Labs
