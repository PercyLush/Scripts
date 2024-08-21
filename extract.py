import PyPDF2

path = "C:\\Users\\Bheki Lushaba\\Downloads\\APPM323_Module Plan 2024 - Kamogelo Makuapane.pdf"

with open(path, "rb") as file1:
    data = PyPDF2.PdfReader(file1)

    Text = ""

    for page in range(1, 1):
        pages = data.pages[page]
        text = pages.extract_text()
        Text += text

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Scripts\\APPM323.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)