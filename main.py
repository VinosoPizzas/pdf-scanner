from pdf2image import convert_from_path
from random import randrange

for i in range(0,49):
    pdfs = (r"C:\Users\Vinícius C. Ruzenent\Documents\pdfs\PDFS\\"+str(i)+".pdf")
    pages = convert_from_path(pdfs, 350)
    j = 1
    for page in pages:
        image_name = "Page_" + str(randrange(1000)) + ".jpg"
        page.save(str(randrange(1000))+image_name, "JPEG")
        j = j+1