from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from groceryDAO import groceryDAO

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#  curl "http://127.0.0.1:5000"
@app.route('/')
@cross_origin()
def index():
    return "Welcome to Grocery API!"

# curl "http://127.0.0.1:5000/items"
@app.route('/items')
@cross_origin()
def getAll():
    return jsonify(groceryDAO.getAll())

@app.route('/items/<int:id>')
@cross_origin()
def findById(id):
    item = groceryDAO.findByID(id)
    return jsonify(item) if item else abort(404)

@app.route('/items', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400, description="Request must be JSON")

    required_fields = ['name', 'category', 'price']
    for field in required_fields:
        if field not in request.json:
            abort(400, description=f"Missing field: {field}")

    try:
        item = {
            "name": request.json['name'],
            "category": request.json['category'],
            "price": float(request.json['price']),
        }
    except ValueError:
        abort(400, description="Invalid price value")

    return jsonify(groceryDAO.create(item))

@app.route('/items/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    item = groceryDAO.findByID(id)
    if not item:
        abort(404)

    data = request.json
    try:
        if 'name' in data:
            item['name'] = data['name']
        if 'category' in data:
            item['category'] = data['category']
        if 'price' in data:
            item['price'] = float(data['price'])
    except ValueError:
        abort(400, description="Price must be a number")

    return jsonify(groceryDAO.update(id, item))

@app.route('/items/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    groceryDAO.delete(id)
    return jsonify({'done': True})

if __name__ == '__main__':
    app.run(debug=True) 