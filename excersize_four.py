# shapes and texts
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#img[200:300, 100:200] = 255,0,0

cv2.line(img,(0, 0),(300,300),(0, 255, 255),3)
cv2.line(img,(0, 0),(img.shape[1], img.shape[0]),(0, 255, 255),3)
cv2.rectangle(img,(0,0),(250,350),(0,0, 255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img, "Moj tekst",(200,100), cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),1)

cv2.imshow("Image", img)


cv2.waitKey(0)