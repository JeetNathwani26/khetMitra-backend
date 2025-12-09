from file.database import get_db
import requests
import json
import os

class Admin:
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
    
        file_path=r"C:\khetmitra\khetmitra-manager\public\user.json"
        with open(file_path, "r") as file:
            users = json.load(file)

        for i, user in enumerate(users):
            if user.get("email") == user_email and user.get("role") == user_role:
                del users[i]  
                break 

        with open(file_path, "w") as file:
            json.dump(users, file, indent=4)
        return {"message": "User verified and removed!", "data": user}
    
    def status(self,user_mail,status,rol):
            update = self.collection.update_one(
                {"email": user_mail,"role":rol},
                {"$set": {"status": status}}
            )
            return update

    def delete_user(self, user_email, user_role):
        result = self.collection.delete_one({"email": user_email, "role": user_role})
        return result
    
    def verify_user(self,token):
            secret = "6LcYIeYrAAAAAAWGnmAczw6S-7AGCkMytjhYbljF"  # Replace with your reCAPTCHA secret key
            url = "https://www.google.com/recaptcha/api/siteverify"
            payload = {'secret': secret, 'response': token}
            response = requests.post(url, data=payload).json()
            return response.get("success", False)

    
    

