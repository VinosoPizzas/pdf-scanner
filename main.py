from PdfScanner import *
import pytesseract

img = PdfScanner("505Page_688.jpg")
img.render_window()
