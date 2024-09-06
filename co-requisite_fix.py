import json

def make_prerequisite_same():
    path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University Of Western Cape.json"

    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            # Ensure Prerequisite exists and is not None
            for key in ["Prerequisite", "Corequisite"]:
                if key in item and item[key]:
                    # If there is more than one prerequisite, wrap them in a $and condition
                    if len(item[key]) > 1:
                        item[key] = [{"$and": item[key]}]

    with open(path, "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)

def standardize():
    path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University Of Western Cape.json"
    
    with open(path, "r", encoding="utf-8") as file1:
        data = json.load(file1)

        for item in data:
            for key in ["Prerequisite", "Corequisite"]:
                if key in item and item[key]:
                    # If there is exactly one prerequisite, extract it from the list
                    if isinstance(item[key], list):
                        if len(item[key]) == 1:
                            item[key] = item[key][0]

    with open(path, "w", encoding="utf-8") as file2:
        json.dump(data, file2, indent=2)

make_prerequisite_same()
standardize()
