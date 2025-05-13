import mysql.connector
import config as cfg


# Lab 07.2 Python and Databases
class GroceryDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.db_config['host']
        self.user=       cfg.db_config['user']
        self.password=   cfg.db_config['password']
        self.database=   cfg.db_config['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql="SELECT * from items"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="SELECT * FROM items WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, item):
        cursor = self.getcursor()
        sql="INSERT INTO items (name, category, price) values (%s,%s,%s)"
        values = (item.get("name"), item.get("category"), item.get("price"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        item["id"] = newid
        self.closeAll()
        return item


    def update(self, id, item):
        cursor = self.getcursor()
        sql="UPDATE items set name= %s, category = %s, price = %s  WHERE id = %s"
        print(f"update item {item}")
        values = (item.get("name"), item.get("category"), item.get("price"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql= "DELETE FROM items WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("delete done")

    def convertToDictionary(self, resultLine):
        attkeys=['id','name','category', 'price']
        item = {}
        currentkey = 0
        for attrib in resultLine:
            item[attkeys[currentkey]] = attrib
            currentkey += 1
        return item
    
groceryDAO = GroceryDAO()  