import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Iamyogi2224",
        database="vehicle_telemetry"
    )
