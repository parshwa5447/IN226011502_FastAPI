# FastAPI Assignment 1

## 📌 Project Overview

This project demonstrates the development of a **RESTful API using FastAPI**.
The API simulates a simple **E-commerce Product Store** where users can view products, filter them by category, search products, and get store insights.

The assignment includes multiple endpoints that showcase different API functionalities such as filtering, searching, and summarizing product data.

---

## ⚙️ Technologies Used

* Python
* FastAPI
* Uvicorn
* REST API

---

## 📂 Project Structure

```
YOUR_UNIQUE_INTERNID_FASTAPI
│
└── Assignment-1
    ├── main.py
    ├── README.md
    ├── Output Screenshots
```

---

## 🚀 How to Run the Project

1. Install dependencies

```
pip install fastapi uvicorn
```

2. Run the FastAPI server

```
uvicorn main:app --reload
```

3. Open the API documentation in browser

```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

### 1️⃣ Get All Products

```
GET /products
```

Returns a list of all products along with the total product count.

---

### 2️⃣ Filter Products by Category

```
GET /products/category/{category_name}
```

Returns products that belong to a specific category.

Example:

```
/products/category/Electronics
```

---

### 3️⃣ Show Only In-Stock Products

```
GET /products/instock
```

Returns only products that are currently available.

---

### 4️⃣ Store Summary

```
GET /store/summary
```

Returns store information including:

* Total products
* In-stock products
* Out-of-stock products
* Available categories

---

### 5️⃣ Search Products by Name

```
GET /products/search/{keyword}
```

Searches products by keyword in product name (case-insensitive).

Example:

```
/products/search/mouse
```

---

### 6️⃣ Cheapest & Most Expensive Product

```
GET /products/deals
```

Returns:

* **Best Deal** → Cheapest product
* **Premium Pick** → Most expensive product

---

## 📊 Example API Output

Example request:

```
GET /products/deals
```

Example response:

```
{
 "best_deal": {
   "name": "Notebook",
   "price": 150
 },
 "premium_pick": {
   "name": "Smartphone",
   "price": 25000
 }
}
```

---

## 📷 Assignment Output

Screenshots of API responses for each question are included in the **Assignment-1 folder**.

---

## 👨‍💻 Author

**Parshwa Desai**

---

## 📜 License

This project was created for **educational and internship assignment purposes**.
