import cv2
import pytesseract

image = cv2.imread('img_kevin_mps.jpg')
data = pytesseract.image_to_string(image, lang=None,config='--psm 6')
print(data)

#cv2.imshow('close', close)
cv2.imshow('thresh', image)
cv2.waitKey()