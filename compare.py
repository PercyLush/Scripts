import json

# Define file paths
path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of Free State.json"
path2 = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\output.json"

# Load the JSON data from both files
with open(path, "r", encoding="utf-8") as file1, open(path2, "r", encoding="utf-8") as file2:
    data = json.load(file1)
    data2 = json.load(file2)

    for item in data:
        if "Name" not in item or item["Name"] == item["Code"]:
            for item2 in data2:
                if item["Code"] == item2["Code"]:
                    item["Name"] = item2["Name"]

# Write the updated data back to the first file
with open(path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)
