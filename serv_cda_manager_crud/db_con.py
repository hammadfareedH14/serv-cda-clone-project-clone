import pymongo
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()  # Make sure to load the environment variables

# Access the environment variables
MONGO_URL = os.getenv('MONGO_URL')
MONGO_DB_ATLAS = os.getenv('MONGO_DB_ATLAS')

class connection:
    @staticmethod
    def db_client_atlas():
        if not MONGO_DB_ATLAS or not isinstance(MONGO_DB_ATLAS, str):
            raise ValueError("MONGO_DB_ATLAS environment variable is not set or is not a valid string")
        
        client = MongoClient(MONGO_URL)
        db = client[MONGO_DB_ATLAS]  # This will now raise an error if MONGO_DB_ATLAS is None or not a string
        
        return db
