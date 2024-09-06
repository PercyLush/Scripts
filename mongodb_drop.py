from pymongo import MongoClient

Client = MongoClient("")
db = Client["RocketScience"]
collection = db["course"]

delete = ["", "TO BE UPDATED", ["N/A"]]
keys = ["Corequisite", "Prequisite", "Assessments"]

for dele in delete:
    for key in keys:
        result = collection.update_many(
            {key: dele},
            {"$unset": {key: ""}}
        )
        if result.modified_count > 0:
            print(f"{key} with Value '{dele}' dropped! ({result.modified_count} documents updated)")
