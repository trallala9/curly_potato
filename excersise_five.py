#get prespective image

import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")



cv2.imshow("Image", img)

cv2.waitKey(0)