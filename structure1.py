import re

path = "C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\SUN-EMS.txt"

def separate():
    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(\d{5}(.+))"
        new_data = re.sub(pattern, r"Subject: \1", data)

    with open(path, "w", encoding="utf-8") as file2:
        file2.write(new_data)

def make_data_representable():
    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(\d{3}\s*\((.+))"
        new_data = re.sub(pattern, r"\n\n\n\1", data)

    with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\testing.txt", "w", encoding="utf-8") as file2:
        file2.write(new_data)

separate()
make_data_representable()