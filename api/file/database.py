from pymongo import MongoClient

def get_db(db_name):
    try:
        uri = (
            "mongodb+srv://jeetnathwani660_db_user:nnnkmHRmDFlyrIx0@cluster0.mc28jjy.mongodb.net/?appName=Cluster0"
        )

        client = MongoClient(uri)
        db = client[db_name]
        return db

    except Exception as e:
        raise Exception(f"Failed to connect to MongoDB: {e}")
