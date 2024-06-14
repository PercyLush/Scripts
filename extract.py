import PyPDF2

path = "c:\\Users\\Bheki Lushaba\\Downloads\\2024-Engineering (1).pdf"

with open(path, "rb") as file1:
    data = PyPDF2.PdfReader(file1)

    Text = ""

    for page in range(60, 100):
        pages = data.pages[page]
        text = pages.extract_text()
        Text += text

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\SUN-Engineering.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)