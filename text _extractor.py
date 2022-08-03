import PyPDF2
a=PyPDF2.PdfFileReader('sample.pdf')
print(dir(PyPDF2.PdfFileReader))
print(a.getNumPages())
str=""
for i in range(0,2):
    str+=a.getPage(1).extractText()

with open("text.txt","w",encoding='utf-8') as f:
    f.write(str)