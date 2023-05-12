from flask import Flask, request, abort
import json
from config import db
from flask_cors import CORS
from bson import ObjectId

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
    if "Title" not in data or len(data["Title"]) < 3:
        return abort(400, "Title is required and should have at least 3 characters")
    if not isinstance(data["Price"], (int, float)):
        return abort(400, "Price must be a number")
    if data["Price"] <= 0:
        return abort(400, "Price is required and should be greater than 0")
    if "Category" not in data:
        return abort(400, "Category must be selected")
    db.products.insert_one(data)
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


@app.get("/api/products/byid/<id>")
def get_by_id(id):
    db_id = ObjectId(id)
    product = db.products.find_one({"_id": db_id})
    if product is None:
        return abort(404, "Product not found")
    return json.dumps(fix_id(product))


@app.delete("/api/products/<id>")
def delete_product(id):
    db_id = ObjectId(id)
    db.products.delete_one({"_id": db_id})
    return json.dumps({"status": "OK", "message": "Product successfully deleted"})

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
    existing_coupon = db.coupons.find_one({"coupon_code": data["coupon_code"]})
    if existing_coupon is not None:
        return abort(409, "Coupon code already exists")
    if "coupon_code" not in data or len(data["coupon_code"]) < 4:
        return abort(400, "Coupon code must exist and be at least 4 characters")
    if not isinstance(data["coupon_discount"], (int, float)):
        return abort(400, "Coupon discount must be a number")
    if not (5 < data["coupon_discount"] < 70):
        return abort(400, "Coupon discount must be between 5 and 70")
    db.coupons.insert_one(data)
    return json.dumps(fix_id(data))


@app.get("/api/coupons/<code>")
def get_coupon_code(code):
    coupon = db.coupons.find_one({"coupon_code": code})
    if not coupon:
        return abort(404, "Invalid coupon code")
    return json.dumps(fix_id(coupon))


@app.delete("/api/coupons/<code>")
def delete_coupon(code):
    db.coupons.delete_one({"coupon_code": code})
    return json.dumps({"status": "OK", "message": "Coupon code successfully deleted"})


# app.run(debug=True)
