import json
import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    
    for item in data:
        if "Code" in item:
            item["Code"] = item["Code"].replace(" ", "")

with open(path, "w", encoding="utf-8") as file2:
    json.dump(data, file2, indent=2)
