# Ref: Lab 6.01 - Creating your own API with Flask

from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from groceryDAO import groceryDAO

categories = [
    {"id": 1, "name": "Fruit"},
    {"id": 2, "name": "Vegetables"},
    {"id": 3, "name": "Dairy"},
    {"id": 4, "name": "Bakery"},
    {"id": 5, "name": "Meat"},
    {"id": 6, "name": "Cereal"},
    {"id": 7, "name": "Toiletries"},
    {"id": 8, "name": "Beverage"},
    {"id": 9, "name": "Cleaning"},
    {"id": 10, "name": "Baking"}
    ]

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    return "Welcome to Grocery API!"

# GET all items
@app.route('/items', methods=['GET'])
@cross_origin()
def getAll():
    return jsonify(groceryDAO.getAll())

# GET item by id
@app.route('/items/<int:id>', methods=['GET'])
@cross_origin()
def findById(id):
    item = groceryDAO.findByID(id)
    if not item:
        abort(404, description="Item not found")
    return jsonify(item)

# Create all new items
@app.route("/items", methods=["POST"])
def create():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data or "category_id" not in data:
        abort(400, description="Missing required fields")

    item = {
        "name": data["name"].strip(),
        "price": data["price"],
        "category_id": data["category_id"]
    }

    new_item = groceryDAO.create(item)
    created_item = groceryDAO.findByID(new_item["id"])  # fetch with category name
    return jsonify(created_item)

#Update item
@app.route('/items/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    item = groceryDAO.findByID(id)
    if not item:
        abort(404, description="Item not found")

    data = request.get_json(force=True)
    if not data:
        abort(400, description="Missing JSON body")

    if 'name' in data:
        item["name"] = data["name"].strip()
    if 'price' in data:
        item["price"] = data["price"]
    if 'category_id' in data:
        item["category_id"] = data["category_id"] 

    groceryDAO.update(id, item)
    updated_item = groceryDAO.findByID(id)  # get fresh updated item (with category name)

    category = groceryDAO.findByID(updated_item["category_id"])
    updated_item["category"] = category["name"] if category else "Unknown"
    return jsonify(updated_item)

# Delete item
@app.route('/items/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    item = groceryDAO.findByID(id)
    if not item:
        abort(404, description="Item not found")

    groceryDAO.delete(id)
    return jsonify({"result": True})

# Get categories
@app.route('/categories', methods=['GET'])
@cross_origin()
def get_categories():
    return jsonify(categories)

if __name__ == '__main__':
    app.run(debug=True) 