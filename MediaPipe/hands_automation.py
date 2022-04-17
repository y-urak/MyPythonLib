import math
import cv2
import mediapipe as mp
import time
import autopy
import numpy as np

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

    # 手の情報の取得＋画面表示
    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # selfにするとどの場所（関数）でも使えるようになる
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    # 手の座標情報の取得
    def findPosition(self,img,handNo=0,draw=True):
        self.lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id,cx,cy])
                if draw:
                    # id,0 or 9 13 9
                    if id==8 or id==4:
                        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        return self.lmList

    # 縦が0 -> 右がマイナス　左がプラス
    # https://qiita.com/Hoshi_7/items/d04936883ff3eb1eed2d
    def reviseHandlmList(self,img,draw=True):
        deg=0
        if len(self.lmList)>0:
            tmp1=[(self.lmList[9][1]+self.lmList[13][1])/2, (self.lmList[9][2]+self.lmList[13][2])/2]
            rad = math.atan2(self.lmList[0][2]-tmp1[1],self.lmList[0][1]-tmp1[0]) - math.pi/2
            deg = rad*180/math.pi
            #print(deg)
            # あんまりうまく変換できていない
            for lm in self.lmList:
                p0_x = lm[1] * math.cos(-rad) - lm[2] * math.sin(-rad)
                p0_y = lm[1] * math.sin(-rad) - lm[2] * math.cos(-rad)
                if draw:
                    cv2.circle(img, (abs(int(p0_x)),abs(int(p0_y))), 10, (0, 0, 255), cv2.FILLED)
        return deg


    # 右手か左手かの情報の取得
    def getHandedness(self, img, handNo=0, draw=True):
        self.handednessList = []
        if self.results.multi_hand_landmarks:
            self.handednessList.append(self.results.multi_handedness[handNo].classification[0].label)
            if draw:
                cv2.putText(img, str(self.handednessList[0]), (100, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    #findPosition のlmlistを使っている
    def fingersUp(self):
        fingers = []
        # thumb
        if self.results.multi_hand_landmarks:
            if self.handednessList[0]=="Left":
                if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
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

    def check_handsign(self,img,draw=True):
        return_handsign=""
        if len(self.lmList)>0:
            fingers=self.fingersUp()
            dist = calc_distance(self.lmList)
            if fingers[0]==1 and fingers[1]==1 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
                return_handsign="paper"
            elif fingers[0]==0 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
                return_handsign="rock"
            elif fingers[0]==0 and fingers[1]==1 and fingers[2]==1 and fingers[3]==0 and fingers[4]==0:
                return_handsign="scissors"
            elif dist<7 and fingers[1]==0 and fingers[2]==1 and fingers[3]==1 and fingers[4]==1:
                #dist=calc_distance(self.lmList)
                #print(dist)
                #if dist<7:
                return_handsign = "ok"
            elif fingers[0]==1 and fingers[1]==0 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
                return_handsign="back"
            elif fingers[0]==0 and fingers[1]==1 and fingers[2]==0 and fingers[3]==0 and fingers[4]==0:
                return_handsign="direction"
            if draw:
                cv2.putText(img, str(return_handsign), (250, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        return return_handsign

# 親指の先と人差し指の先の距離を出す
def calc_distance(ar,no1=4,no2=8):
    d = math.sqrt((ar[no1][1]-ar[no2][1])**2+(ar[no1][2]-ar[no2][2])**2)
    #print(d)
    return d

def autopy_input(sign,deg,cons,cnt):
    if sign=="ok" and cons==0:
        autopy.key.toggle(autopy.key.Code.DOWN_ARROW, True, [])
        autopy.key.tap(autopy.key.Code.DOWN_ARROW, [], 0.05)
        cons=1
    # autopyでキー入力
    elif sign=="direction":
        if deg < -5:
            if (cnt) % int(np.interp(deg, [-45, -5], [1, 8])) == 0:
                autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, True, [])
                autopy.key.tap(autopy.key.Code.RIGHT_ARROW, [], 0.05)
        elif deg > 5:
            if (cnt) % int(np.interp(deg, [5, 45], [8, 1])) == 0:
                autopy.key.toggle(autopy.key.Code.LEFT_ARROW, True, [])
                autopy.key.tap(autopy.key.Code.LEFT_ARROW, [], 0.05)
    elif sign=="back" and cons==1:
        # ctrl+F4
        # https://support.google.com/chrome/answer/157179?hl=ja&co=GENIE.Platform%3DDesktop#zippy=%2C%E3%82%BF%E3%83%96%E3%81%A8%E3%82%A6%E3%82%A3%E3%83%B3%E3%83%89%E3%82%A6%E3%81%AE%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%82%AB%E3%83%83%E3%83%88
        autopy.key.toggle(autopy.key.Code.CONTROL, True, [])
        autopy.key.toggle(autopy.key.Code.F4, True, [])
        autopy.key.tap(autopy.key.Code.CONTROL, [], 0.1)
        autopy.key.tap(autopy.key.Code.F4, [], 0.1)
        #autopy.key.type_string("tt")
        cons = 0
    return cons


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector=handDetector()
    cnt=0
    totalF=0
    whereis = 0
    while True:
        sccess, img = cap.read()
        # ------------------------------------
        img=detector.findHands(img)
        detector.findPosition(img)
        detector.getHandedness(img)
        Sign=detector.check_handsign(img)
        print(detector.fingersUp()) # 開いているかどうか
        Deg=detector.reviseHandlmList(img,draw=False)
        whereis=autopy_input(Sign,Deg,whereis,cnt)
        #--------------------------------------
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        totalF+=fps
        # print(totalF/cnt)
        cnt+=1
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()