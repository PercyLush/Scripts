from pymongo import MongoClient
import json

Client = MongoClient("")
db = Client["gradesmatch_core"]
collection = db["user"]

pattern = r"([A-z]+(.+))"
registered_institutions = []

results = collection.find({
    "RegisteredInstitution": {
        "$regex": pattern, "$options": "i"
    }
})

for result in results:
    print(result)