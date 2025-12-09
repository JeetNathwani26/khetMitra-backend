from file.database import get_db
from google.oauth2 import id_token # pyright: ignore[reportMissingImports]
from google.auth.transport.requests import Request   # type: ignore
from flask import  jsonify
from bson import ObjectId # type: ignore
import json
import os

ID = "656820879847-4qtalivq7nitn908s0ossdatvecf8df6.apps.googleusercontent.com"



class user:
    def __init__(self,user):
        self.db=get_db(db_name="khetmitra")
        self.collection=self.db[user]

    def add_data(self,data):
        result=self.collection.insert_one(data)
        return str(result.inserted_id) 
    
    def get_data(self):
        data=list(self.collection.find({}))
        for doc in data:
            doc["_id"]=str(doc["_id"])

        return data 
    
    def gets_data(self,data,mail):
        data=self.collection.find_one({'emails':mail,'sendemail':data})

        return data

    def update_proposal_status(self, proposal_id, status):
        from bson.objectid import ObjectId # type: ignore
        update = self.collection.update_one(
            {"_id": ObjectId(proposal_id)},
            {"$set": {"status": status}}
        )
        return update.modified_count > 0
    
    def password(self,user_mail,password):
            update = self.collection.update_one(
                {"email": user_mail},         
                {"$set": {"password":password}}   
            )
            return update
    
    def google(token):
        try:
            if not token:
                return jsonify({"error": "Missing token"})

            # ✅ Correct way: use Request() from google.auth.transport.requests
            idinfo = id_token.verify_oauth2_token(token, Request(), ID)

            user_data = idinfo.get("email")

            return user_data
        except ValueError:
            return jsonify({"error": "Invalid token"}), 401
        
    def get_user_documents(self, documents):
        
        return list(documents)
    
    def report(self,data):
        result=self.collection.insert_one(data)
        return str(result.inserted_id)
    
    def get_report(self):
        data=list(self.collection.find({"status": "Pending"}))
        for doc in data:
            doc["_id"]=str(doc["_id"])

        return data
    
    def update(self,use_id,status):
        
        update = self.collection.update_one(
            {"_id": ObjectId(use_id)},
            {"$set": {"status": status}}
        )
        return update.modified_count > 0


