import json

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\North West University.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    Text = ""

    for item in data:
        type = []
        for key in ["Assessments", "Assessment1"]:
            if key in item:
                for assessment in item[key]:
                    type.append(assessment["Type"])
                if "Exam" not in type:
                    Text += f'{item["Code"]} - No Examination\n'
with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Courses_without_Exam.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)