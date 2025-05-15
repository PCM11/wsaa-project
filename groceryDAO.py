import pymysql
import config as cfg

class GroceryDAO:
    connection = ""
    cursor = ""
    host = ""
    user = ""
    password = ""
    database = ""

    def __init__(self):
        self.host = cfg.db_config['host']
        self.user = cfg.db_config['user']
        self.password = cfg.db_config['password']
        self.database = cfg.db_config['database']
        self.create_table()

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

    def create_table(self):
        cursor = self.getcursor()
        sql = """
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                category VARCHAR(100),
                price FLOAT
            )
        """
        cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM items"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM items WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDictionary(result) if result else None

    def create(self, item):
        cursor = self.getcursor()
        sql = "INSERT INTO items (name, category, price) VALUES (%s, %s, %s)"
        values = (item.get("name"), item.get("category"), item.get("price"))
        cursor.execute(sql, values)
        self.connection.commit()
        new_id = cursor.lastrowid
        item["id"] = new_id
        self.closeAll()
        return item

    def update(self, id, item):
        cursor = self.getcursor()
        sql = "UPDATE items SET name = %s, category = %s, price = %s WHERE id = %s"
        values = (item.get("name"), item.get("category"), item.get("price"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM items WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def convertToDictionary(self, resultLine):
        attkeys = ['id', 'name', 'category', 'price']
        item = {}
        for i, value in enumerate(resultLine):
            item[attkeys[i]] = value
        return item

# Instantiate
groceryDAO = GroceryDAO()
