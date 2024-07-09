from pymongo import MongoClient
import json

Client = MongoClient("mongodb+srv://gradesmatch:gm55Y3nmoGdRFdd3s@gradesmatchdev.seham.mongodb.net/test?retryWrites=true&w=majority")
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