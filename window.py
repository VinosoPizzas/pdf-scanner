import cv2 as cv

img = cv.imread(cv.samples.findFile("img_kevin_mps.jpg"))
if img is None:
    sys.exit("Could not read the image.")

scale_percent = 18 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
cv.imshow("Display window", resized)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("img_kevin_mps.jpg", img)