import json
import re

path1 = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\Stellenbosch University.json"
path2 = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output22.json"


with open(path1, "r") as file1, open(path2, "r", encoding="utf-8") as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

    for item1 in data1:
        if "Code" in item1:
            for item2 in data2:
                remove_number = r"(\d+)"
                new_name = re.sub(remove_number, r"", item1["Name"])
                new_name = new_name.strip()

                if new_name == item2["SubjectName"]:
                    get_number = r"(\d+)"
                    match = re.search(get_number, item1["Code"])
                    if match:
                        code = item2["Code"] + f"-{match.group()}"
                        item1["Code"] = code

with open("Testing.json", "w", encoding="utf-8") as file:
    json.dump(data1, file, indent=2)
