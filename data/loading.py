import psycopg2
import json
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def insert_weather_data(conn, data):
    with conn.cursor() as cur:
        for weather_data in data:
            cur.execute("""
                INSERT INTO weather (city, temperature, humidity, pressure, weather_description, datetime)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (weather_data['city'], weather_data['temperature'], weather_data['humidity'], weather_data['pressure'], weather_data['weather_description'], weather_data['datetime']))
        conn.commit()

def insert_traffic_data(conn, data):
    with conn.cursor() as cur:
        for route in data:
            cur.execute("""
                INSERT INTO traffic (summary, distance, duration, start_address, end_address, start_location, end_location, steps)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (route['summary'], route['distance'], route['duration'], route['start_address'], route['end_address'], json.dumps(route['start_location']), json.dumps(route['end_location']), json.dumps(route['steps'])))
        conn.commit()
        
def select_weather_data(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM weather")
        weather_data = cur.fetchall()
    return weather_data

def select_traffic_data(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM traffic")
        traffic_data = cur.fetchall()
    return traffic_data