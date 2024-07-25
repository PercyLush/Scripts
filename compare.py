import json

# Define file paths
path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of Free State.json"
path2 = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\UFS_Names+CodesFinal.json"

# Load the JSON data from both files
with open(path, "r", encoding="utf-8") as file1, open(path2, "r", encoding="utf-8") as file2:
    data = json.load(file1)
    data2 = json.load(file2)

    # Create a lookup dictionary from the second file for quick access
    code_to_name = {item2["Code"]: item2["Name"] for item2 in data2 if "Code" in item2 and "Name" in item2}

    # Update the 'Name' field in the first file based on matching 'Code'
    for item in data:
        if "Code" in item and "Name" in item:
            if item["Code"] in code_to_name:
                item["Name"] = code_to_name[item["Code"]]

# Write the updated data back to the first file
with open(path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2)
