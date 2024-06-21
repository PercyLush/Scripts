from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://percybheki3:8cGbRGgs9FCPOwdA@isitthou.agweefv.mongodb.net/")
db = cluster["RocketScience"]
collection = db["ItIsNot"]

user_name = "percybheki3"
existing_user = collection.find_one({"user_name": user_name})

if existing_user:
    result = collection.update_one(
        {"user_name": user_name},
        {"$set": {"service": "MongoDB"}}
    )
    print("Updated")
else:
    print("Does not exist")