from pymongo import MongoClient  # type: ignore

def get_db(db_name):
    uri = (
        "mongodb+srv://jeetnathwani660_db_user:YfvCmokx5AZMOX5T"
        "@cluster0.mc28jjy.mongodb.net/?retryWrites=true&w=majority"
    )

    client = MongoClient(uri)
    return client[db_name]
