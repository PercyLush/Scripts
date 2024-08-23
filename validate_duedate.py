import json
import re

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University Of Pretoria.json"

with open(path, "r", encoding = "utf-8") as file1:
    data = json.load(file1)
    
    Text = ""

    def validate(assessment):
        global Text

        if "DueDate" in assessment:
            pattern = r"(\d{4}-\d{2}-\d{2})"
            match = re.search(pattern, assessment["DueDate"])

            if match:
                duedate = assessment["DueDate"].split("-")
                year = duedate[0]
                month = duedate[1]
                day = duedate[2]

                if year != "2024":  
                    Text += f'{item["Code"]} - Year not 2024\n{assessment["Name"]}\n\n'

                if not (1 <= int(month) <= 12):
                    Text += f"{item['Code']} - Invalid Month\n{assessment['Name']}\n\n"
                if not (1 <= int(day) <= 31):
                    Text += f"{item['Code']} - Invalid Day\n{assessment['Name']}\n\n"

    for item in data:
        for key in ["Assessments", "Assessment1"]:
            if key in item:
                for assessment in item[key]:
                    validate(assessment)

                    if "Subitems" in assessment:
                        for subitem in assessment["Subitems"]:
                            validate(subitem)

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Invalid_DueDates.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)