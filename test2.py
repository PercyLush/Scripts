import json

def find_indentation(line):
    # Count the number of leading spaces
    return len(line) - len(line.lstrip())

path = "C:\\Users\\Bheki Lushaba\\course-data\\CourseData_Final\\University of Johannesburg.json"

with open(path, "r", encoding="utf-8") as file1:
    lines = file1.readlines()

data = json.loads(''.join(lines))
codes_seen = {}
to_delete = []

for idx, line in enumerate(lines):
    if '"Code":' in line:
        code = line.split(':')[1].strip().strip('",')
        indentation = find_indentation(line)
        
        if code in codes_seen:
            prev_idx, prev_indentation = codes_seen[code]
            if indentation > prev_indentation:
                to_delete.append(idx)
            else:
                to_delete.append(prev_idx)
                codes_seen[code] = (idx, indentation)
        else:
            codes_seen[code] = (idx, indentation)

# Create a set of indices to delete for quick lookup
to_delete_set = set(to_delete)

# Remove the lines with the greater indentation
new_lines = [line for idx, line in enumerate(lines) if idx not in to_delete_set]

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\Testing.json", "w", encoding="utf-8") as file1:
    file1.writelines(new_lines)

print(f"Removed {len(to_delete_set)} lines with greater indentation.")
