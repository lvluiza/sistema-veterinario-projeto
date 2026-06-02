import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="grupo5@",
            database="vet_db"
        )
        return connection
    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None