# reference : https://www.youtube.com/watch?v=01sAkU_NvOY&list=LL&index=20&t=3013s&ab_channel=freeCodeCamp.org

import cv2
import numpy
import numpy as np
import HandTrackingModule as htm
import time
import autopy



##################################
wCam, hCam = 640,480
wScr, hScr =autopy.screen.size()
frameR = 100 #Frame Reducion
#自分でいじって滑らかさを返る部分 5,7,10,20
soothening=7
##################################
plocX,plocY=0,0
clocX,clocY=0,0
##print(wScr,hScr)

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

pTime = 0
detector = htm.handDetector()

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
    if len(lmList) != 0:
        # 2.  Get the tip of the index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        print(fingers)
        # 4. Only Index Finger : Moving Mode
        if fingers[1]==1 and fingers[2]==0:
            pass
            # 5. Convert Coodicates
            # パディング分に注意
            x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
            # 6. Smoothen Values
            clocX=plocX+(x3-plocX)/soothening
            clocY=plocY+(y3-plocY)/soothening
            # 7. Move Mouse
            ##逆に動くから引く
            autopy.mouse.move(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocX,plocY=clocX,clocY
        # 8. Both Index and middle fingers are up : Clicking Mode
        elif fingers[1] == 1 and fingers[2]==1:
            length=numpy.sqrt((x1-x2)^2+(y1-y2)^2)
            print(length)
            # 10. Click mouse if distance short
            if length<2.5:
            #if fingers[0] == 1:
                cv2.circle(img, (int((x1+x2)/2), int((y1+y2)/2)), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
            elif hScr / 2 > plocY and fingers[3] == 1:
                autopy.key.toggle(autopy.key.Code.UP_ARROW, True, [])
            elif hScr / 2 < plocY and fingers[3] == 1:
                autopy.key.toggle(autopy.key.Code.DOWN_ARROW, True, [])

        # 11. Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    # 12. Display
    cv2.imshow("Image",img)
    cv2.waitKey(1)
