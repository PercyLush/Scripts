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

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\UFS_Names+CodesFinal.json"    

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    for item in data:
        if "Code" in item:
            item["Code"] = item["Code"].replace(" ", "")
        
        if "Name" in item:
            pattern = r"(\d{4}\s*)"
            item["Name"] = re.sub(pattern, r"", item["Name"])
                
with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\UFS_Names+CodesFinal.json" , "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)