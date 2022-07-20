from PyPDF2 import PdfWriter, PdfReader

reader = PdfReader("materials/97-98.pdf")
page = reader.pages[0]
print(page.cropbox.upper_right)