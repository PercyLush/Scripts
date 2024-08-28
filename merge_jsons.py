import json
import shutil

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\cput_course_data.json"
course_data = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\Cape Peninsula University of Technology.json"
backup_course_data = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Cape Peninsula University of Technology_backup.json"

# Create a backup of the original course_data
shutil.copy(course_data, backup_course_data)

try:
    with open(path, "r", encoding="utf-8") as file1, open(course_data, "r", encoding="utf-8") as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
        
        data1_dict = {item["Code"]: item for item in data1}
        
        for item2 in data2:
            code = item2.get("Code")
            if code and code in data1_dict:
                item1 = data1_dict[code]

                if "Assessments" in item1 and "Assessments" in item2:
                    print(f'{item2["Code"]} Has Assessments') # Codes with assessments on both JSON files

                for key in ["Duration", "Period", "NQF", "Credit", "Prerequisite", "Corequisite", "Description", "Assessments"]:
                    if key in item1 and key not in item2:
                        item2[key] = item1[key]
                if "Description" in item1:
                    item2["Description"] = item1["Description"]

    with open(course_data, "w", encoding="utf-8") as file:
        json.dump(data2, file, indent=2)
    
    print("Data merging completed successfully.")
    
except FileNotFoundError as e:
    print(f"Error: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
