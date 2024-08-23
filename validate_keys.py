import json

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University Of Western Cape.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    KEYS = ["_id", "Name", "DP", "Code", "NQF", "AlternativeCode", "Passmark", "Passmarks", "Year","Credit", "Duration", "Period", "Prerequisite", "Corequisite", "Assessments", "Assessment1", "Description", "Institution"]
    Text = ""

    for item in data:
        code = item.get("Code", "Code Unknown")
        for key, value in item.items():
            if key not in KEYS:
                if "Code" in item:
                    Text += f'{code} - Invalid Key: {key}\n\n'

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Invalid_Keys.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)
