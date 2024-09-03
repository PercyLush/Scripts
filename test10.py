import json

path = "C:/Users/Bheki Lushaba/course-data/CourseData_Final/University of Limpopo.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Name" in item:
            if item["Name"].isupper():
                item["Name"] = item["Name"].title()
with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)