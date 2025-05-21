# Ref: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html
# Ref: Lab 07.01 Databases
# Ref: Lab 07.2 Python and Databases 

import pymysql
import config as cfg

class GroceryDAO:

    def __init__(self):
        self.host = cfg.db_config['host']
        self.user = cfg.db_config['user']
        self.password = cfg.db_config['password']
        self.database = cfg.db_config['database']
        self.create_cattable()
        self.create_itemtable()

    def getcursor(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.Cursor
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.cursor.close()
        self.connection.close()

    # Create tables
    # Categories table was designed with guidance from ChatGPT(OpenAI).
    # Prompt: "How to connect tables in MYSQL"
    
    def create_cattable(self):
        cursor = self.getcursor()
        sql = """
        CREATE TABLE IF NOT EXISTS categories (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        )
        """
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

    def create_itemtable(self):
        cursor = self.getcursor()

        # Create items table with category_id foreign key
        sql = """
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                category_id INT,
                price FLOAT NOT NULL,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
            )
        """
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

    # Read all items
    def getAll(self):
        cursor = self.getcursor()
        sql = """
            SELECT items.id, items.name, items.category_id, categories.name AS category, items.price
            FROM items
            JOIN categories ON items.category_id = categories.id

        """
        cursor.execute(sql)
        results = cursor.fetchall()
        items = []
        for row in results:
            items.append(self.convertToDictionary(row))
    
        self.closeAll()
        return items

    # Find items by ID
    def findByID(self, id):
        cursor = self.getcursor()
        sql = """
        SELECT items.id, items.name, items.category_id, categories.name AS category, items.price
            FROM items
            LEFT JOIN categories ON items.category_id = categories.id
            WHERE items.id = %s
        """
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        self.closeAll()
        if result:
           return dict(zip([desc[0] for desc in cursor.description], result))
        return None
    
    # Get category ID
    def get_cat_id(self, category_name):
        cursor = self.getcursor()
        sql = "SELECT id FROM categories WHERE name = %s"
        cursor.execute(sql, (category_name,))
        result = cursor.fetchone()

        if result:
            category_id = result[0]
        else:
            insert_sql = "INSERT INTO categories (name) VALUES (%s)"
            cursor.execute(insert_sql, (category_name,))
            self.connection.commit()
            category_id = cursor.lastrowid

        self.closeAll()
        return category_id

    # Create new item
    def create(self, item):
        cursor = self.getcursor()
        sql = "INSERT INTO items (name, category_id, price) VALUES (%s, %s, %s)"
        values = (item.get("name"), item.get("category_id"), item.get("price"))
        cursor.execute(sql, values)
        self.connection.commit()
        item["id"] = cursor.lastrowid
        self.closeAll()
        return item

    # Update item
    def update(self, id, item):
        cursor = self.getcursor()
        sql = "UPDATE items SET name = %s, category_id = %s, price = %s WHERE id = %s"
        values = (item.get("name"), item.get("category_id"), item.get("price"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    # Delete item
    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM items WHERE id = %s"
        cursor.execute(sql, id)
        self.connection.commit()
        self.closeAll()

    # Get categories
    def get_categories(self):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM categories")
        return cursor.fetchall()

    def convertToDictionary(self, row):
        attkeys = ['id', 'name', 'category_id', 'category', 'price']
        item = {}
        
        if row: 
            for key, value in zip(attkeys, row):
                item[key] = value

        return item

# Instantiate
groceryDAO = GroceryDAO()
