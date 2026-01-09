import mysql.connector 
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sangamesh19",
    database="student_analytics"
)

# print(conn)
cursor = conn.cursor()