import re
import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output22.json"

def separate():
    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            pattern = r"(\n(.+))"
            item["Code"] = re.sub(pattern, r"", item["Code"])

    with open(path, "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)

separate()