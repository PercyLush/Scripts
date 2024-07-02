import json

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\Regent Business School.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    
    
    for item in data:
        if "Code" in item:
            item["Code"] = item["Name"]
        
with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)
