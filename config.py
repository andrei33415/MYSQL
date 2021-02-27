import mysql.connector
def connect():
    return  mysql.connector.connect( 
            host="localhost",
            user="root",
            passwd="root",
            )

#comanda install: pip install mysql-connector-python