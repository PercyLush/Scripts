import json
from datetime import datetime


path1 = "C:\\Users\\Bheki Lushaba\\Desktop\\gradesmatch_core.usercourse.json"


with open(path1, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:

        if "Assessments" in item and item["Assessments"] != None:
            for assessment in item["Assessments"]:

                if "DueDate" in assessment:
                    assessment["dueDate"] = assessment["DueDate"]
                    del assessment["DueDate"]

with open(path1, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)