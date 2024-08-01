import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\data2.txt"

with open(path, "r", encoding="utf-8") as file1:
    data = file1.read()

    code_pattern = r"([A-Z]+\s*\d{4})\s*(.+)"

    final_data = re.sub(code_pattern, r"Code: \1\nName: \2\n", data)

with open(path, "w", encoding="utf-8") as file:
    file.write(final_data)