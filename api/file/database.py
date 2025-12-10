from pymongo import MongoClient  # type: ignore

def get_db(db_name):
    client = MongoClient(
        "mongodb+srv://jeetnathwani660_db_user:YfvCmokx5AZMOX5T@cluster0.mc28jjy.mongodb.net/"
        "?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true"
    )
    db = client[db_name]
    return db
