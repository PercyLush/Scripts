import json

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\cput_course_data.json"

with open(path, "r", encoding="utf-8") as file1:
    data1 = json.load(file1)
    
    for item in data1:
        if "Code" not in item:
            if "Description" in item:
                print(f'Code +++++ {item["Description"]}')
            else:
                print(f'Previous Code - {item["Description"]} - No Name and Code')