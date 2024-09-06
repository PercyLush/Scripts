from pymongo import MongoClient
import getpass

name = input("enter user_name: ")
password = getpass.getpass("enter password: ")
service = input("serive/app name: ")

client = MongoClient("")
db = client["RocketScience"]
collection = db["ItIsNot"]

collection.insert_one(
    {"user_name": name,"password": password,"service": service}
    )
