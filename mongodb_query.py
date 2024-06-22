from pymongo import MongoClient

Client = MongoClient("mongodb+srv://percybheki3:8cGbRGgs9FCPOwdA@isitthou.agweefv.mongodb.net/")
db = Client["RocketScience"]
collection = db["ItIsNot"]

pattern = r"percy"

result_collection = collection.find({
    "user_name": {
        "$regex": pattern, "$options": "i"
        }
    }
)

for x in result_collection:
    print(x)
print("done!")

# Find documents where the address starts with the letter "S" or higher:
# myquery = { "address": { "$gt": "S" } }
# mydoc = mycol.find(myquery)