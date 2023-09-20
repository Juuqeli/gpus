from pymongo import MongoClient
import psycopg2
from psycopg2.extras import RealDictCursor
from config import settings

#connecting to MongoDB with PyMongo
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client.gpus
collection = db.torihtml

#Connecting to PostgreSQL database with psycopg2
try:
    conn = psycopg2.connect(host = settings.database_hostname, dbname = settings.database_name, user = settings.database_username, password = settings.database_pwd, cursor_factory = RealDictCursor)
    cursor = conn.cursor()
    print('Database connection succesful')
except Exception as e:
    print(f'connection failed: {e}')