import json

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\North West University.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    Text = ""

    for item in data:
        if "Assessments" not in item:
            Text += f'{item["Code"]} - No Assessments\n'
        else:
            if "Assessments" in item:
                if len(item["Assessments"]) <= 2:
                    Text += f'{item["Code"]} - Assessments Insufficient\n'

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\NorthWest_Assessments.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)