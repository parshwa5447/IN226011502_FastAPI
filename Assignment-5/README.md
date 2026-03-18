# FastAPI Assignment 5 – Search, Sort & Pagination System

## 📌 Project Overview

This project implements advanced API features using **FastAPI**, including:

* Product Search (case-insensitive)
* Sorting (price & name)
* Pagination
* Combined filtering (Search + Sort + Pagination)
* Orders search functionality
* Category-based sorting
* Orders pagination (Bonus)

The API simulates a real-world **E-commerce browsing system**.

---

# ⚙️ Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic

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

### Open API Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📂 Project Structure

```
IN226011502_FASTAPI
│
├── Assignment-1
├── Assignment-2
├── Assignment-3
├── Assignment-4
└── Assignment-5
    ├── main.py
    ├── README.md
    └── Output (Screenshots)
```

---

# 🔍 API Endpoints

## 1️⃣ Search Products

```
GET /products/search
```

Query Param:

* `keyword`

Example:

```
/products/search?keyword=mouse
```

✔ Case-insensitive search
✔ Returns matching products and total count
✔ Returns message if no products found

---

## 2️⃣ Sort Products

```
GET /products/sort
```

Query Params:

* `sort_by` → price / name
* `order` → asc / desc

Example:

```
/products/sort?sort_by=price&order=asc
```

✔ Default → sort_by=price, order=asc
✔ Invalid sort returns error

---

## 3️⃣ Pagination

```
GET /products/page
```

Query Params:

* `page`
* `limit`

Example:

```
/products/page?page=1&limit=2
```

✔ Supports multiple pages
✔ Returns total_pages

---

## 4️⃣ Search Orders

```
GET /orders/search
```

Query Param:

* `customer_name`

Example:

```
/orders/search?customer_name=rahul
```

✔ Case-insensitive search
✔ Returns matching orders
✔ Returns message if no results

---

## 5️⃣ Sort by Category + Price

```
GET /products/sort-by-category
```

✔ Sorts by category (A → Z)
✔ Then sorts by price within category

---

## 6️⃣ Combined Endpoint (Real API)

```
GET /products/browse
```

Query Params:

* `keyword` (optional)
* `sort_by` (default = price)
* `order` (default = asc)
* `page` (default = 1)
* `limit` (default = 4)

Example:

```
/products/browse?keyword=e&sort_by=price&order=asc&page=1&limit=2
```

✔ Filter → Sort → Paginate
✔ All parameters optional

---

# ⭐ Bonus Feature – Orders Pagination

```
GET /orders/page
```

Query Params:

* `page` (default = 1)
* `limit` (default = 3)

✔ Used to browse large order lists
✔ Returns total_pages

---

# ❌ Error Handling

### Invalid Sort

```json
{
  "error": "sort_by must be 'price' or 'name'"
}
```

### No
