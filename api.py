from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin

from grocery_DAO import groceryDAO

app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
@cross_origin()
def index():
    return "Welcome to Grocery API!"

#curl "http://127.0.0.1:5000/"items
# GET all items
@app.route('/items', methods=['GET'])
@cross_origin()
def get_items():
    #print("in getall")
    results = groceryDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/groceries/2"
# GET grocery by ID
@app.route('/items/<int:id>')
@cross_origin()
def findById(id):
    foundItem = groceryDAO.findByID(id)
    return jsonify(foundItem)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books
# POST a new grocery item
@app.route('/items', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)

    # other checking 
    item = {
        "name": request.json['name'],
        "category": request.json['category'],
        "price": request.json['price'],
    }
    addedItem = groceryDAO.create(item)
    return jsonify(addedItem)

# PUT update grocery item
@app.route('/groceries/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundItem = groceryDAO.findByID(id)
    if not foundItem:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'name' in reqJson:
        foundItem['name'] = reqJson['name']
    if 'category' in reqJson:
        foundItem['category'] = reqJson['category']
    if 'price' in reqJson:
        foundItem['price'] = reqJson['price']

    groceryDAO.update(id,foundItem)
    return jsonify(foundItem)

# DELETE a grocery item
@app.route('/items/<int:id>' , methods=['DELETE'])
@cross_origin()
def delete(id):
    groceryDAO.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)