from pymongo import MongoClient

client = MongoClient("")
db = client["RocketScience"]
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
client.close()