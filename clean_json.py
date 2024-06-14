import json
import re

def name():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output22.json"

    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            item["SubjectName"] = item["SubjectName"].strip()

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output22.json", "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)