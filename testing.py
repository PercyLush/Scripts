import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Testing.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    
    course_counts = {}
    
    for item in data:
        if "Code" in item:
            code = item["Code"]
            if code in course_counts:
                course_counts[code] += 1
            else:
                course_counts[code] = 1
with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Testing2.json", "w", encoding="utf-8") as file2:
    json.dump(course_counts, file2, indent=2)
