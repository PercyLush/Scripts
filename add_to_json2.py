import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\cput_course_data.json"
course_data = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\Cape Peninsula University of Technology.json"

with open(path, "r", encoding="utf-8") as file1, open(course_data, "r", encoding="utf-8") as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)


    existing_codes = {item["Code"] for item in data2}


    for item1 in data1:
        if item1["Code"] not in existing_codes:
            data2.append(item1)
            existing_codes.add(item1["Code"])  # Update the set to include the newly added code


with open(course_data, "w", encoding="utf-8") as file:
    json.dump(data2, file, indent=2)

print("Data merging completed successfully.")
