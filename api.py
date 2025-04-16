# python packages
from flask import Flask, request, url_for, redirect, abort

# Initiating a Flask application
app = Flask(__name__, static_url_path='', static_folder='staticpages')

#data = request.get_json()
#books = {
 #       'id': data['id'],
  #      'title': data['title'],
   #     'author': data['author'],
    #    'published_year': data['published_year']
    #}

@app.route('/')
def index():
    return "Book List"

# The endpoint of our flask app
@app.route('/books', methods=['GET']) 
def get_books():
    return "This is the GET Endpoint Of Flask"

@app.route('/books/<int:id>', methods=['GET']) 
def find_book(id): 
    return "find by id" 

#create, read json from the body
@app.route('/books', methods=['POST']) 
def create_book():
    jsonstring = request.json
    return f"create {jsonstring}"

# update 
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    jsonstring = request.json 
    return f"update {id} {jsonstring}"

#delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    return f"delete {id}"

# Running the API
if __name__ == "__main__":
    app.run(debug=True)


