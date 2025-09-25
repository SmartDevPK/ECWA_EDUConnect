import os
from dotenv import load_dotenv
import mysql.connector

# Load environment variables from a .env file
load_dotenv()

connection = None
cursor = None

try:
    # Connect to the server
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3307)), 
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )
    # Create a cursor and execute a query
    cursor = connection.cursor()
    cursor.execute("SELECT CURDATE()")
    row = cursor.fetchone()
    print(f"current date is: {row[0]}")

finally:
    # Always close cursor and connection if they were created
    if cursor:
        cursor.close()
    if connection:
        connection.close()
