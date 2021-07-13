#resizing image
import cv2
import numpy as np

img = cv2.imread("resources/orange.jpg")
print(img.shape)

imgResize = cv2.resize(img,(300,200))

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)

cv2.waitKey(0)