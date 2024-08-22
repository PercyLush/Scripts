import json

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of Venda.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    Text = ''
    for item in data:
        if "Name" not in item or item["Name"] == "":
            if "Code" in item:
                Text += f"{item['Code']}\n"

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\no_name_courses.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)