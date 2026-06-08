# Não esquecer de instalar o conector do MySQL para Python(NO TERMINAL):
# python -m pip install mysql-connector-python

import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3306,
            password="Gaiguinho10@",
            database="vet_db"
        )
        return connection
    except mysql.connector.Error as e:
        print("Database connection error:", e)
        return None
    

