import json

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of Free State.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    Text = ""
    for item in data:
        if "Code" in item and "Name" in item:
            if item["Code"] == item["Name"]:
                Text += f"{item['Code']}\n"
with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\UFS_Duplicated_Codes+Names.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)
