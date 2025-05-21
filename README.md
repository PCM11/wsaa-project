# Grocery API

<img src="https://mvp.dev/wp-content/uploads/2023/06/Differentiating-SaaS-and-Web-Applications.png" width="700" height="400">

## Overview

This is a simple RESTful API built with **Flask** and **MySQL** for managing grocery items. It also includes a basic HTML/Javascript frontend to interact with the API and is deployed on [pythonAnywhere](https://www.pythonanywhere.com/).

**Live App:** [https://pcm11.pythonanywhere.com/](https://pcm11.pythonanywhere.com/)

## Structure

| File             | Description                                |
|------------------|--------------------------------------------|
| `app_server.py`  | Main Flask server handling the API.        |
| `groceryDAO.py`  | MySQL Data Access Object (DAO) layer.      |
| `config.py`      | Stores database credentials and connection info. Make sure to add your own DB config here.|
| `items.html`     | Frontend HTML interface to view, create, update and delete grocery items.|
| `requirements.txt`| List of Python packages needed to run the project (Flask, flask-cors, pymysql, etc.).|

## Requirements

Download and install [Python](https://www.python.org/downloads/) and [MYSQL](https://www.python.org/downloads/).

## Getting Started

**1. Clone the repository:**

```bash
git clone https://github.com/PCM11/wsaa-project
```

**2. Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate 
```

**3.Install dependencies:**

```bash
pip install -r requirements.txt
pip install flask, flask-cors
pip install pymysql
```

**4. Configuration:**
Create a config.py file in the root directory with the with your credentials:

```python
# config.py
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'database'
}
```

**5. Run the App Locally:**

```bash
python app_server.py
```

Open items.html in your browser or access it via the server at:
<http://127.0.0.1:5000/items.html>

## API Endpoints

Method	    | Endpoint	       | Description 
----------- | -----------------| ----------- 
GET         | /                | Welcome message
GET	        | /api/items	   | Get all grocery items 
GET	        | /api/items/<id>  | Get item by ID 
POST	    | /api/items	   | Create a new item 
PUT	        | /api/items/<id>  | Update an existing item |
DELETE	    | /api/items/<id>  | Delete an item |

API returns JSON responses and expects JSON-formatted request bodies for POST and PUT requests.

## Deploying to PythonAnywhere

- Upload all files to PythonAnywhere project directory.

- Install required modules via pip (use --user on PythonAnywhere)

- Update your WSGI file to import from app_server.py

Set the WSGI file to:

```python
import sys
path = '/home/PCM11/grocery-deploy'
if path not in sys.path:
    sys.path.insert(0, path)

from app_server import app as application
```

- Reload the web app from the **Web** tab.

## Acknowledgements

The sample code for this project can be found on: [https://github.com/andrewbeattycourseware/deploytopythonanywhere]

Assistance from OpenAI's ChatGPT (GPT-4.5) was used to debug the code and prompt-based guidance was used to connect items table and categories table.
Tool used: [ChatGPT by OpenAI](https://chat.openai.com/)

## Author
Phumi Tshidi