import json

path = r"C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Courses.json"
output_path = r"C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\CoursesFinal.json"


with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    new_data = []
    
    for item1 in data:
        if "CourseCode" in item1:
            if not any(item2["CourseCode"] == item1["CourseCode"] for item2 in new_data):
                new_data.append(item1)

with open(output_path, "w", encoding="utf-8") as file2:
    json.dump(new_data, file2, indent=2)

print("Data saved successfully to CoursesFinal.json.")
