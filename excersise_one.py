import cv2
print('Package cv2 has been imported')


#### IMPORT OBRAZKA ####
#img = cv2.imread('resources/kot.png')
#cv2.imshow('Output', img)
#cv2.waitKey(0)

#### IMPORT VIDEO ####
#cap = cv2.VideoCapture('resources/banana.mp4')
#while True:
    #success, img = cap.read()
    #cv2.imshow('Video', img)
    #if cv2.waitKey(1) & 0xFF ==ord('q'):
        #break

#### WEBCAM Detection ###
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,80)

while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break