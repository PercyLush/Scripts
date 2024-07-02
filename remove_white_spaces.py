import json

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\North West University.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        for key in ["Name", "Description"]:
            if key in item:
                item[key] = item[key].replace("  ", " ")

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)