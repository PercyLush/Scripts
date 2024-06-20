import PyPDF2

path = "C:\\Users\\Bheki Lushaba\\Downloads\\2024-EMS (1).pdf"

with open(path, "rb") as file1:
    data = PyPDF2.PdfReader(file1)

    Text = ""

    for page in range(202, 265):
        pages = data.pages[page]
        text = pages.extract_text()
        Text += text

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\SUN-EMS.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)