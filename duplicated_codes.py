import json

# Define the file paths
input_path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of Free State.json"
output_path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Duplicates_Count.txt"

# Read the JSON file
with open(input_path, "r", encoding="utf-8") as file1:
    data = json.load(file1)
    course_count = {}
    
    for item in data:
        course_code = item.get("Code")
        if course_code:
            if course_code in course_count:
                course_count[course_code] += 1
            else:
                course_count[course_code] = 1

output_text = ""
for course, count in course_count.items():
    output_text += f'{course} +{count}\n'

with open(output_path, "w", encoding="utf-8") as file2:
    file2.write(output_text)
