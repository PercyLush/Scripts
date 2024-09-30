import json

path = "C:/Users/Bheki Lushaba/Desktop/Scripts/Extracted_Codes.json"

with open(path, "r", encoding="utf-8") as file1:
    data = json.load(file1)

    Codes = [item["Code"]  for item in data]
    Codes = list(set(Codes))

with open("C:/Users/Bheki Lushaba/Desktop/Scripts/Extracted_Codes_no_Duplicates.json", "w") as file2:
    json.dump(Codes, file2, indent=2)