from pymongo import MongoClient
import psycopg2
from psycopg2.extras import RealDictCursor
from config import settings

#connecting to MongoDB with PyMongo
client = MongoClient("mongodb://127.0.0.1:27017/")
mongo_dbs = client.list_database_names()
db = client.gpus
coll_name = "tori"
collection = db[coll_name]

if __name__ == "__main__":
    def create_collection():
        mongo_document_validator = {
            "$jsonSchema": {
                "bsonType": "object",
                "title": "Scraped data validation",
                "required": [ "html_content", "source", "load_time"],
                "properties": {
                    "html_content": {
                    "bsonType": "string",
                    "description": "'html_content' must be a string and is required"
                    },
                    "source": {
                    "bsonType": "string",
                    "description": "'source' must be a descriptive string and is required"
                    },
                    "load_time": {
                    "bsonType": "date",
                    "description": "'load_time' must be a datetime and is required"
                    }
                }
            }
        }

        try:
            db.create_collection(coll_name)
            print(f"Succesfully added collection(s) {db.list_collection_names()} to MongoDB")
        except Exception as e:
            print(e)

        db.command("collMod", coll_name, validator=mongo_document_validator)

    create_collection()

    #Connecting to PostgreSQL database with psycopg2
    try:
        conn = psycopg2.connect(host = settings.database_hostname, dbname = settings.database_name, user = settings.database_username, password = settings.database_pwd, cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print('Postgres Database connection succesful')
    except Exception as e:
        print(f'Postgres database connection failed: {e}')