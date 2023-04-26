from flask import Flask, request
import json 
from config import db

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask"

#fix the object to be JSON parsable
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.get("/api/about")
def about():
    me = { "name": "Weeraphot Bumbaugh" }
    return json.dumps(me)

@app.get("/api/catalog")
def get_catalog():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

@app.post("/api/catalog")
def save_product():
    data = request.get_json()
    db.products.insert_one(data)
    print(data)
    return json.dumps(fix_id(data))

# sum of all price
@app.get("/api/total")
def get_total():
    cursor = db.products.find({})
    total = 0
    for prod in cursor:
        total += prod["Price"]
    return json.dumps(total)

# total # of products
@app.get("/api/products")
def total_products():
    cursor = db.products.find({})
    products = 0
    for prod in cursor:
        products += 1
    return json.dumps(products)

app.run(debug=True)