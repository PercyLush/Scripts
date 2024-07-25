import re
import json

def text_file():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\data.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(UGRD\s*S1\s*|UGRD\s*S2\s*|UGRD\s*YR\s*)"

        new_file = re.sub(pattern, r"Code: ", data)
    with open(path, "w", encoding="utf-8") as file2:
        file2.write(new_file)

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\UFS_Names+Codes.json"    

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Code" in item:
            pattern = r"([A-Z]+\s*\d{4})"
            Code = item["Code"]
            code = re.search(pattern, code)
            if code:
                item["Code"] = code.group()

            pattern_name = r"\d+\s*(.+)"
            name = re.search(pattern_name, code)
            if name:
                item["Name"] = name.group()
                
with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\UFS_Names+CodesFinal.json" , "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)