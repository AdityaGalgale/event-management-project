import mysql.connector as myconn

def connect():
    return myconn.connect(
        host="localhost",
        user="root",        
        password="root",
        database="event_system"
    )
