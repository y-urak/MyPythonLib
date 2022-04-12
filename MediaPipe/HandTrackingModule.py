import cv2
import mediapipe as mp
import time

class handDetector():
    #Handsの引数を最初にひっぱってきて初期化
    #ここに値を入れておくと初期化時にわざわざ値をいれなくても大丈夫
    def __init__(self,mode=False,maxHands=4,detectionCon=0.7,trackCon=0.7):
        self.mode = mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        # mediapipeを使うための変数
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        #指開いているか用
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # selfにするとどの場所（関数）でも使えるようになる
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img,handNo=0,draw=True):
        self.lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape

                cx, cy = int(lm.x * w), int(lm.y * h)

                self.lmList.append([id,cx,cy])

                if draw:
                    cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        return self.lmList
    #Project 4
    def fingersUp(self):
        fingers = []
        # thumb
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 finger
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector=handDetector()
    cnt=1
    totalF=0
    while True:
        sccess, img = cap.read()
        img=detector.findHands(img)
        lmList=detector.findPosition(img)

        #ほしいlandmarkだけの情報をとりだせるようになる
        #if len(lmList) != 0:
           # print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        totalF+=fps
        print(totalF/cnt)
        cnt+=1
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()