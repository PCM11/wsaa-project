# Required packages
from flask import Flask, request, url_for, redirect, abort

# Initiating a Flask application
app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/') 
def index():
    return "Book REST API" 


# The endpoint of our flask app
@app.route('/books', methods=['GET']) 
def getall():
    return "This is the GET Endpoint Of Flask" 

@app.route('/books/<int:id>', methods=['GET']) 
def findbyid(id): 
    return "find by id" 

#create 
@app.route('/books', methods=['POST']) 
def create():
    jsonstring = request.json
    return f"create {jsonstring}" 


# update 
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json 
    return f"update {id} {jsonstring}"

#delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

# Running the API
if __name__ == "__main__":
    app.run(debug=True)


