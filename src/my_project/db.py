import mysql.connector
from mysql.connector import Error

#Creating a database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root'
            database = 'Ecwa_connect'
            password = ''
        )
        if connection.is_connected():
            print("Connection to database was successful")
            return connection            
    except Error as e:
        print(f"Error Connecting to MYSQL: {e} ")
        return None