import json
import re

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of Limpopo.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Description" in item:
            for i in range(1, 138):
                patterm = re.escape(f"{i}")
                item["Description"] = re.sub(patterm, r"", item["Description"])

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)