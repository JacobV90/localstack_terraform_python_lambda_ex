import os
import mysql.connector
from mysql.connector import Error

def get_connection():
  params = {
    'host': os.environ['DB_HOST'],
    'database': os.environ['DB_NAME'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
    'ssl_disabled': True,
  }
  try:
    connection = mysql.connector.connect(**params)
    if connection.is_connected():
      db_Info = connection.get_server_info()
      print("Connected to MySQL Server version ", db_Info)
      cursor = connection.cursor()
      cursor.execute("select database();")
      record = cursor.fetchone()
      print("You're connected to database: ", record)
      return connection
  except Error as e:
    print("Error while connecting to MySQL", e)
    raise

