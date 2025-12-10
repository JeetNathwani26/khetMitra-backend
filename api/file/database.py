import os
from pymongo import MongoClient  # type: ignore
from pymongo.errors import ConnectionFailure

def get_db(db_name):
    try:
        # Use environment variable for MongoDB URI to avoid hardcoding credentials
        uri = os.getenv('MONGODB_URI', 'mongodb+srv://jeetnathwani660_db_user:nnnkmHRmDFlyrIx0@cluster0.mc28jjy.mongodb.net/?appName=Cluster0')
        client = MongoClient(uri)
        # Test the connection
        client.admin.command('ping')
        return client[db_name]
    except ConnectionFailure as e:
        raise Exception(f"Failed to connect to MongoDB: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while connecting to the database: {e}")
