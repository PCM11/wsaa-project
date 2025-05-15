# Web Services an Applications - Project Repository

<img src="https://mvp.dev/wp-content/uploads/2023/06/Differentiating-SaaS-and-Web-Applications.png" width="700" height="400">


## Overview

This repository contains a Flask-based web application that provides a **RESTful API** for interacting with a relational database. It includes both API endpoints and web pages that allow users to perform full **CRUD (Create, Read, Update, Delete)** operations on data stored in one or more database tables.

## REST API Design

**Entity:Book**

Each book has the following attributes:

- `id` (int)
- `name` (string)
- `category` (string)
- `price` (int)

## Features

- RESTful API for data access and manipulation

- Web interface to interact with the API using HTML templates

- Connects to one or more relational database tables

- Full CRUD support: Create, Read, Update, Delete

- Clean separation of frontend and backend concerns

- JSON responses for API consumption

- Clean and modular code structure



## Requirements

Download and install **Python 3.7+**. 

## Getting Started

**1. Clone the repository:**

```bash
git clone https://github.com/your-username/web-services-app.git
cd web-services-app
```

**2. Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate 
```

**3.Install dependencies:**

```bash
pip install -r requirements.txt
pip install Flask
```


**4. Run the application:**

```bash
flask run
```

**5.Test with curl**

```bash
curl http://127.0.0.1:5000/books
```


Then navigate to http://127.0.0.1:5000/ in your browser.

## API Endpoints

Method	    | Endpoint	       | Description 
----------- | -----------------| ----------- 
GET	        | /api/items	   | Retrieve all items 
GET	        | /api/items/<id>  | Retrieve item by ID 
POST	    | /api/items	   | Create a new item 
PUT	        | /api/items/<id>  | Update an item |
DELETE	    | /api/items/<id>  | Delete an item |

API returns JSON responses and expects JSON-formatted request bodies for POST and PUT requests.

## Web Interface

The frontend is built using HTML templates rendered by Flask. Use the UI to:

View all entries in the database

Create new entries via forms

Edit or delete existing entries

The web interface communicates with the backend via both form submissions and AJAX calls to the REST API.
