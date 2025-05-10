
import mysql.connector
#import config as cfg


# Lab 07.2 Python and Databases
# Create 'grocery' database
connection = mysql.connector.connect( 
  host="localhost", 
  user="root", 
  password=""
)

mycursor = connection.cursor()

mycursor.execute("CREATE database grocery")
mycursor.close()
connection.close()

mydb = mysql.connector.connect( 
  host="localhost", 
  user="root", 
  password="", 
  database="grocery" 
) 