import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
color =(244,0,0)

cx,cy,w,h = 100,100,200,200
detector = HandDetector(detectionCon=0.8)
while True: 
    
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    

    if hands:
        lmList = hands[0]['lmList']
        cursor = lmList[8] 
        point1 = lmList[8][:2]
        point2 = lmList[12][:2]

        # Calculate distance between the points
        length, info, img = detector.findDistance(point1, point2, img)


        if cx-w//2 < cursor[0] < cx+w//2 and cy-h//2 < cursor[1] < cy+h//2 and length<65:
            color = (0, 244, 0)  
            cx,cy=cursor[0],cursor[1]
        else:
            color = (244, 0, 0)  

        


    
    cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2, cy+h//2), color, cv2.FILLED)
    cv2.imshow("Image", img)
    cv2.waitKey(1)