import re
import json

def extract_key_value_pairs(file_path):
    import re
    # Open the file and read its content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    keys_of_interest = ["Code"]

    extracted_data_list = []

    pattern = re.compile(r'(\w+):\s*((?:.*(?:\n(?!\w+:).*)*))\n')

    matches = pattern.findall(content)

    current_course_data = {}

    for match in matches:
        key, value = match
        if key in keys_of_interest:
            if key == "Code":
                current_course_data[key] = value

        if key == "Code":
            extracted_data_list.append(current_course_data)
            current_course_data = {}  # Reset for the next course

    return extracted_data_list

# Provide the path to your text file
file_path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\data.txt"

# Call the function to extract key-value pairs
result_list = extract_key_value_pairs(file_path)

# Specify the path for the JSON file
json_file_path = 'UFS_Names+Codes.json'

with open(json_file_path, 'w') as json_file:
    json.dump(result_list, json_file, indent=2)

print(f"Data has been successfully stored in {json_file_path}")
