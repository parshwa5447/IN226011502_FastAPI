from fastapi import FastAPI
from dotenv import load_dotenv
import os

#Load .env file
load_dotenv()

#Read environment variables
APP_NAME = os.getenv("APP_NAME") or "Product Store API"
APP_VERSION = os.getenv("APP_VERSION") or "1.0"

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

products = [
    {"id": 1, "name": "Smartphone", "price": 25000, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Headphones", "price": 2000, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Coffee Mug", "price": 300, "category": "Home", "in_stock": True},
    {"id": 4, "name": "Notebook", "price": 150, "category": "Stationery", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1200, "category": "Accessories", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 4500, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1800, "category": "Electronics", "in_stock": True}
]

@app.get("/")
def home():
    return {"message": "Welcome to Product Store API"}

@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

#Question 2:-
#Category Filter Endpoint
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered_products = [
        product for product in products
        if product["category"].lower() == category_name.lower()
    ]

    if not filtered_products:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": filtered_products,
        "total": len(filtered_products)
    }

#Question 3:-
#In-Stock Products Endpoint
@app.get("/products/instock")
def get_instock_products():

    instock_products = [
        product for product in products
        if product["in_stock"] == True
    ]

    return {
        "in_stock_products": instock_products,
        "count": len(instock_products)
    }

#Question 4:-
#Store Summary Endpoint
@app.get("/store/summary")
def store_summary():

    total_products = len(products)

    in_stock_count = len([p for p in products if p["in_stock"] == True])
    out_of_stock_count = len([p for p in products if p["in_stock"] == False])

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }

#Question 5:-
#Product Search Endpoint
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    matched_products = [
        product for product in products
        if keyword.lower() in product["name"].lower()
    ]

    if not matched_products:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "matched_products": matched_products,
        "total_matches": len(matched_products)
    }

#Bonus:-
# Cheapest & Most Expensive Product Endpoint
@app.get("/products/deals")
def product_deals():

    best_deal = min(products, key=lambda x: x["price"])
    premium_pick = max(products, key=lambda x: x["price"])

    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }