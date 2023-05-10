from flask import Flask, request, abort
import json
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # disable CORS security rule


@app.get("/")
def home():
    return "Hello from Flask"

# fix the object to be JSON parsable


def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj


@app.get("/api/about")
def about():
    me = {"name": "Weeraphot Bumbaugh"}
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


@app.get("/api/categories")
def get_categories():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        cat = prod["Category"]
        if cat not in products:
            products.append(cat)
    return json.dumps(products)


@app.get("/api/category/<name>")
def get_by_category(name):
    products = []
    cursor = db.products.find({"Category": name})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)


@app.get("/api/products/search/<text>")
def get_by_title(text):
    products = []
    cursor = db.products.find({"Title": {"$regex": text, "$options": "i"}})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)


@app.get("/api/products/lower/<price>")
def get_by_lower(price):
    products = []
    cursor = db.products.find({"Price": {"$lt": float(price)}})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)


@app.get("/api/products/greater/<price>")
def get_by_greater(price):
    products = []
    cursor = db.products.find({"Price": {"$gte": float(price)}})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

############### COUPONS ####################


@app.get("/api/coupons")
def get_coupons():
    coupons = []
    cursor = db.coupons.find({})
    for coup in cursor:
        coupons.append(fix_id(coup))
    return json.dumps(coupons)


@app.post("/api/coupons")
def save_coupon():
    data = request.get_json()
    db.coupons.insert_one(data)
    print(data)
    return json.dumps(fix_id(data))


@app.get("/api/coupons/<code>")
def get_coupon_code(code):
    coupon = db.coupons.find_one({"coupon_code": code})
    if not coupon:
        return abort(404, "Invalid coupon code")
    return json.dumps(fix_id(coupon))


@app.delete("/api/coupons/<code>")
def delete_coupon(code):
    result = db.coupons.delete_one({"coupon_code": code})
    if result.deleted_count == 0:
        return abort(404, "Invalid coupon code")
    return json.dumps({"status": "OK", "message": "Coupon code successfully deleted"})

# app.run(debug=True)
