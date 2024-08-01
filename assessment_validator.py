import json
import os
import glob

def assessment_validate(My_List):
    invalid_assessments = ""
    for item in My_List:
        count = 0
        if "Assessments" in item:
            for assessment in item["Assessments"]:
                if "Subitems" in assessment:
                    subitems_weight = 0
                    all_subitems_have_weights = True
                    for subitem in assessment["Subitems"]:
                        if "Weight" in subitem:
                            subitems_weight += subitem["Weight"]
                        else:
                            all_subitems_have_weights = False
                    if all_subitems_have_weights:
                        count += subitems_weight
                    else:
                        if "Weight" in assessment and (isinstance(assessment["Weight"], int) or isinstance(assessment["Weight"], float)):
                            count += assessment["Weight"]
                        else:
                            invalid_assessments += f"{item.get('Institution', 'Unknown')}-{item['Code']} Weight not available\n"
                else:
                    if "Weight" in assessment and (isinstance(assessment["Weight"], int) or isinstance(assessment["Weight"], float)):
                        count += assessment["Weight"]
                    else:
                        invalid_assessments += f"{item.get('Institution', 'Unknown')}-{item['Code']} Weight not available\n"

            if count != 100:
                invalid_assessments += f"{item.get('Institution', 'Unknown')}-{item['Code']} \n"
    return invalid_assessments

def read_json_files_from_folder(folder_path):
    json_files = glob.glob(os.path.join(folder_path, "*.json"))
    data = []
    for file_path in json_files:
        with open(file_path, "r", encoding="utf-8") as file:
            data.extend(json.load(file))
    return data

folder_path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final"

data = read_json_files_from_folder(folder_path)

invalid_assessments = assessment_validate(data)

output_file_path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Assessment_Validate.txt"
with open(output_file_path, "a", encoding="utf-8") as file2:
    file2.write(invalid_assessments)

print(f"Validation results written to {output_file_path}")
