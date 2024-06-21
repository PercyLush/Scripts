from pymongo import MongoClient

Client = MongoClient("mongodb+srv://percybheki3:8cGbRGgs9FCPOwdA@isitthou.agweefv.mongodb.net/")
db = Client["RocketScience"]
collection = db["ItIsNot"]

service = "Gmail"
existing_database = collection.find_one({"service": service})

if existing_database:

    result = collection.update_one({
        "service": service
        },
        {
            "$set": {
                "password": "***"
            }
        }
        )
    print("Password Deleted")
else:
    print("Could not find service")