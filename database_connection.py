import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sangamesh19",
        database="student_analytics"
    )
