import json

path = "C:/Users/Bheki Lushaba/Desktop/gradesmatch_core.usercourse_prod.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    Courses = []

    for item in data:
        code = {}
        if "CourseCode" in item:
            code = {"Institution": item["Institution"],"CourseCode": item["CourseCode"]}
            Courses.append(code)
    
with open("C:/Users/Bheki Lushaba/Desktop/Scripts/Courses.json", "w", encoding="utf-8") as file2:
    json.dump(Courses, file2, indent=2)