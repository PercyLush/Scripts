import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://percybheki3:<password>@cluster0.pfpvmz4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["HelloWorld"]
collection = db["Testing"]

collection.insert_one({})