from pymongo import MongoClient  # type: ignore

def get_db(db_name):
    client=MongoClient("mongodb+srv://jeetnathwani660_db_user:YfvCmokx5AZMOX5T@cluster0.mc28jjy.mongodb.net/?appName=Cluster0")
    db=client[db_name]
    return db