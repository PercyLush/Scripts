import json
import re

def name():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output.json"

    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            pattern_number = r"(\d{5})"

            item["SubjectCode"] = re.sub(pattern_number, r"", item["Subject"])
            item["SubjectCode"] = item["SubjectCode"].strip()

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output22.json", "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)

def code():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output22.json"

    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            pattern_number = r"([A-z]+\s*\((.+)+\)|[A-z]+)"

            item["Code"] = re.sub(pattern_number, r"", item["Subject"])
            item["Code"] = item["Code"].strip()

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output22.json", "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)

name()
code()