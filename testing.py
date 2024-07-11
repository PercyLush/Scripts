from pymongo import MongoClient

Client = MongoClient("")
db = Client["Folder_Name"]
collection = db["Collection_List"]


