from pymongo import MongoClient
import json
import re

json_path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University Of Pretoria.json"

Client = MongoClient("mongodb+srv://percybheki3:8cGbRGgs9FCPOwdA@isitthou.agweefv.mongodb.net/")
db = Client["RocketScience"]
collection = db["course"]

institution = "University of Pretoria"
existing_database = collection.count_documents({"Institution": institution})

if existing_database > 0:
    print(f"Institution '{institution}' found in the database.")
    
    with open(json_path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            if "Code" in item:
                # Construct the regex pattern
                pattern = f"^{item['Code']}$"
                
                # Find the document with the matching code (case-insensitive)
                code_match = collection.find_one({"Code": {"$regex": pattern, "$options": "i"}, "Institution": institution})

                if code_match:
                    print(f"Match found for Code: {item['Code']}. Updating the document.")
                    # Delete the existing document
                    collection.delete_one({"_id": code_match["_id"]})
                else:
                    print(f"No match found for Code: {item['Code']}. Inserting as a new document.")
                
                # Insert the new document
                item["Institution"] = institution  # Ensure the institution is set in the new document
                collection.insert_one(item)
                print(f"Document with Code: {item['Code']} inserted.")
else:
    print(f"Institution '{institution}' not found in the database.")

# Close the MongoDB connection
Client.close()