from pdf2image import convert_from_path
from random import randrange

pdfs = f"C:\\Users\\Vinícius C. Ruzenent\\Documents\\pdfs\\barion.pdf"
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "Page_" + str(randrange(1000)) + ".jpg"  
    page.save(str(randrange(1000))+image_name, "JPEG")
    i = i+1      