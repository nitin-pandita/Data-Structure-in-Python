import cv2
from cvzone.HandTrackingModule import HandDetector
import math

# For the webcam
cap = cv2.VideoCapture(0)
cap.set(3,1200)
cap.set(4,720)

# ? Hand Detection
detector = HandDetector(detectionCon=0.8, maxHands=1)

# loop
while True:
    success , img = cap.read()
    hand, img = detector.findHands(img)

    # if hand is present then show the values
    if hand:
        lmList = hand[0]["lmList"]

        #  we going to compare the distance between two finger that is 5 and 17 these are the points that are already given in the mediapipe
                
        x1,y1 = lmList[5]
        x2,y2 = lmList[17]

        distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

        print(abs(x2 - x1), distance)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
