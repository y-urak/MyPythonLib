'''
autopyとmediapipeでGUIを動かすプログラム
GUI: https://editor.p5js.org/ura/sketches/2JXIdDyd-
'''

# FaceMeshNodd + IUsePose
# 重心移動は CoGMovedのみ
import cv2
import mediapipe as mp
import time
from collections import deque
import autopy
import math

#1030 MediaPipe固有のUIの表示
import numpy as np


def showPoseGUI(results,img,mpDraw,mpPose):
    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

#1030 rtrn string 前の鼻の座標と今の座標を比較してどっちに動いているかを計算して方向を返す
def decideDirection(results,img,dString,base=10):
    global preNose
    h, w, c = img.shape
    dx = results.pose_landmarks.landmark[0].x *w -preNose[0]
    dy = results.pose_landmarks.landmark[0].y *h -preNose[1]
    preNose[0] = results.pose_landmarks.landmark[0].x * w
    preNose[1] = results.pose_landmarks.landmark[0].y * h
    returnString ="N"
    if dString=="Ini":
        return returnString
    cv2.putText(img, str(int(dx))+","+str(int(dy)), (int(w / 2), int(h / 2)), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    if abs(dx)<abs(dy):
        if dy<-base:
            cv2.putText(img, "UP" , (int(w / 2), int(h/4)), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
            returnString="U"
        elif dy>base:
            cv2.putText(img, "DOWN" , (int(w / 2), int(h*3/4)), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
            returnString = "D"
    #目の方がいいかも
    elif abs(dx)>abs(dy):
        if dx<-base:
            cv2.putText(img, "LEFT", (int(w / 4), int(h / 2)), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
            returnString = "L"
        elif dx>base:
            cv2.putText(img, "RIGHT", (int(w* 3/ 4), int(h / 2)), cv2.FONT_HERSHEY_PLAIN, 3,
                   (255, 0, 255), 3)
            returnString = "R"
    return returnString

#11 14 rtrn string 前の鼻の座標と今の座標を比較してどっちに動いているかを計算して方向を返す
def decidePointDirection(point,img,dString,base=10):
    global preNose
    h, w, c = img.shape
    dx = point[0] *w -preNose[0]
    dy = point[1] *h -preNose[1]
    preNose[0] = point[0] * w
    preNose[1] = point[1] * h
    returnString ="N"
    if dString=="Ini":
        return returnString
    #cv2.putText(img, str(int(dx))+","+str(int(dy)), (int(w / 2), int(h / 2)), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
    cv2.circle(img, (int(point[0] *w), int(point[1] *h)), 3,(255, 0, 0), 3)
    if abs(dx)<abs(dy):
        if dy<-base:
            cv2.putText(img, "UP" , (int(w / 2), int(h/4)), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
            returnString="U"
        elif dy>base:
            cv2.putText(img, "DOWN" , (int(w / 2), int(h*3/4)), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
            returnString = "D"
    #目の方がいいかも
    elif abs(dx)>abs(dy):
        if dx<-base:
            cv2.putText(img, "LEFT", (int(w / 4), int(h / 2)), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
            returnString = "L"
        elif dx>base:
            cv2.putText(img, "RIGHT", (int(w* 3/ 4), int(h / 2)), cv2.FONT_HERSHEY_PLAIN, 3,
                   (255, 0, 255), 3)
            returnString = "R"
    return returnString

#1030 rtrn int string型で表していた方向を配列の引数に利用できるようにした
def convertD(D):
    i=0
    if D=="U":
        i=1
    elif D=="D":
        i=2
    elif D=="L":
        i=3
    elif D=="R":
        i=4
    return i

#1030 rtrn 数字５つの配列
def dDconvertTotal(dQ):
    cnts=[0,0,0,0,0]
    for i in dQ:
        cnts[convertD(i)]+=1
    return cnts

#1030 rtrn int 頷いている時に1を否定している時に2両方の場合3
# arはN,U,D,L,Rの数
def checkNoddAndRefuse(ar):
    ans=0
    if ar[1]>0 and ar[2]>0:
        ans+=1
    if ar[3]>1 and ar[4]>1:
        ans+=2
    return ans

# ここで判定しているよ！
#1101 コンソールに頷いているか否定しているかを表示する
#1129 autopyでのキー入力追加
# キー入力　
# i=0,1,2,3
def cntNoddAndRefuse(ar):
    global noddTmp,refuseTmp
    i = checkNoddAndRefuse(ar)
    if i==1:
        noddTmp+=1
        #autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, True, [])
        autopy.key.toggle(autopy.key.Code.DOWN_ARROW, True, [])
    elif i==2:
        refuseTmp+=1
        #autopy.key.toggle(autopy.key.Code.UP_ARROW, True, [])

#1101　GUIでテキストを表示する
def showNoddAndRefuseCntGUI(img):
    global noddTmp,refuseTmp
    #pTime = cTime
    # cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,(255,0,0),3)
    cv2.putText(img, "decide : "+str(int(noddTmp)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.putText(img, "cancel : " + str(int(refuseTmp)), (70, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

#重心移動 mpDrawとmpPoseは消せる
def CoGMoved(results,img,trigger):
    rr = r1 = r2 = 0
    ll = l1 = l2 = 0
    counter = 0
    if results.pose_landmarks:
        #mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h_, w_, c_ = img.shape  # ウインドウの大きさ
            # print(h,w)
            # print(id,lm)
            # cx,cy=int(lm.x*frameWidth),int(lm.y*frameHeight)
            cx, cy = int(lm.x * w_), int(lm.y * h_)
            check = False
            # 3,6,9,10,11,12,23,24
            #cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            if counter == 24:
                rr = lm.x * w_
            elif counter == 23:
                ll = lm.x * w_
            elif counter == 26:
                r1 = lm.x * w_
            elif counter == 28:
                r2 = lm.x * w_
            elif counter == 25:
                l1 = lm.x * w_
            elif counter == 27:
                l2 = lm.x * w_
            elif counter == 0:
                preNose[0] = cx
                preNose[1] = cy
            counter += 1

    #if rr > r1 and rr > r2:
    #    cv2.putText(img, 'r', (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    #if ll > l1 and ll > l2:
    #    cv2.putText(img, 'l', (100, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    #if ll < l1 and ll < l2:
    #    cv2.putText(img, 'l', (100, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    #if rr < r1 and rr < r2:
    #    cv2.putText(img, 'r', (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
    #print((rr > r1 and rr > r2) , (rr < r1 and rr < r2),(ll > l1 and ll > l2) , (ll < l1 and ll < l2))
    #TODO :細かい移動がむずすぎー＞細かい移動は首の左右の傾きとかどうですかね？ ー＞一応間隔を広げればよさげ->傾きの大きさの調整でも可とする
    if (rr > r1 and rr > r2) and (ll > l1 and ll > l2) :
        #print("left arrow")
        cv2.putText(img, 'left arrow', (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        #スピードをfps/5の間隔で入力する
        if trigger%7==0:
            #autopy.key.toggle(autopy.key.Code.LEFT_ARROW, True, [])
            #autopy.key.tap(autopy.key.Code.LEFT_ARROW, [], 0.05)
            print("left arrow",trigger)
        return trigger+1
    elif (rr < r1 and rr < r2) and (ll < l1 and ll < l2) :
        #print("right arrow")
        cv2.putText(img, 'right arrow', (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if trigger%5==0:
            print("right arrow",trigger)
            #autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, True, [])
            # delayをいれて調整しよう
            #autopy.key.tap(autopy.key.Code.RIGHT_ARROW, [], 0.05)
        return trigger+1
    else:
        return 0
    #return [w_,h_]

#重心移動 mpDrawとmpPoseは消せる
def Neck_Rotate_inputer(results,img,trigger):
    no0_pos=[]
    no11_pos=[]
    no12_pos=[]
    counter = 0
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h_, w_, c_ = img.shape  # ウインドウの大きさ
            if counter == 0:
                no0_pos.append(lm.x * w_)
                no0_pos.append(lm.y * h_)
            elif counter == 11:
                no11_pos.append(lm.x * w_)
                no11_pos.append(lm.y * h_)
            elif counter == 12:
                no12_pos.append(lm.x * w_)
                no12_pos.append(lm.y * h_)
            counter += 1
        cx, cy = int((no11_pos[0]+no12_pos[0])/2), int((no11_pos[1]+no12_pos[1])/2)


    #TODO :細かい移動がむずすぎー＞細かい移動は首の左右の傾きとかどうですかね？ ー＞一応間隔を広げればよさげ->傾きの大きさの調整でも可とする
    if len(no11_pos)>0:
        x = (- no0_pos[0] + cx)
        y = (- no0_pos[1] + cy)
        r = ((x) ** 2 + (y) ** 2) ** (1 / 2)
        cos = x / r
        sin = y / r
        deg=round(math.degrees(math.acos(cos)) * 1.0)
        #print(deg)
        # 110 ~ 180
        if 100<deg:
            cv2.putText(img, 'right arrow', (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            if (trigger) % int(np.interp(deg,[100 ,170],[12,1])) == 0:
                #print("right : ",int(np.interp(deg,[110 ,180],[10,1])))
                autopy.key.toggle(autopy.key.Code.LEFT_ARROW, True, [])
                autopy.key.tap(autopy.key.Code.LEFT_ARROW, [], 0.05)
            return trigger + 1
        # 0 ~ 70
        elif deg<80:
            cv2.putText(img, 'left arrow', (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            if (trigger) % int(np.interp(deg,[10 ,80],[1,12])) == 0:
                #print(deg,"left : ",int(np.interp(deg,[0 ,70],[1,10])))
                autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, True, [])
                autopy.key.tap(autopy.key.Code.RIGHT_ARROW, [], 0.05)
            return trigger + 1
        else:
            return 0
    #if (rr > r1 and rr > r2) and (ll > l1 and ll > l2) :
            #print("left arrow")
        #    cv2.putText(img, 'left arrow', (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            #スピードをfps/5の間隔で入力する
        #    if trigger%7==0:
                #autopy.key.toggle(autopy.key.Code.LEFT_ARROW, True, [])
                #autopy.key.tap(autopy.key.Code.LEFT_ARROW, [], 0.05)
        #        print("left arrow",trigger)
        #    return trigger+1
        #elif (rr < r1 and rr < r2) and (ll < l1 and ll < l2) :
            #print("right arrow")
        #    cv2.putText(img, 'right arrow', (500, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        #    if trigger%5==0:
        #        print("right arrow",trigger)
                #autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, True, [])
                #autopy.key.tap(autopy.key.Code.RIGHT_ARROW, [], 0.05)
        #    return trigger+1
    else:
        return 0

#今まで表示しているUIの表示
def showFpsGUI(img,pTime,frameWidth):
    global totalFPS,CNT
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    totalFPS+=fps
    #pTime = cTime
    # cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,(255,0,0),3)
    cv2.putText(img, str(int(fps))+" fps", (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    if CNT!=0 : print(totalFPS/CNT)
    return cTime

def main():
    global shoulderBase,noddFlag,noddCnt,noddTmp,noseBase,CNT
    # MediaPipe用 Pose
    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    # Face Mesh
    mpFace = mp.solutions.face_mesh
    face = mpFace.FaceMesh()

    # 無理やりサイズを調整
    frameWidth = 1080
    frameHeight = 900
    #frameWidth = 1080
    #frameHeight = 1500

    # 動画の入力
    #cap =cv2.VideoCapture('video/nodding1.mp4')
    cap = cv2.VideoCapture(0)
    # 形式はMP4Vを指定
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # 出力先のファイルを開く
    out = cv2.VideoWriter("video/nod.m4v", int(fourcc), 10, (int(frameWidth), int(frameHeight)))
    # fps計測用
    pTime = time.time()
    preDirection="Ini"
    totalD=[0,0,0,0,0]
    #　サイズ変更可能
    dDsize=15
    #　第二引数でサイズ指定しているので追加すれば勝手にpopする
    dD=deque([],dDsize)

    #勝手に入力されるようにしないために
    arrow_trigger=0

    while True:
        success, img = cap.read()
        img = cv2.resize(img, (frameWidth, frameHeight))
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # MediaPipe Poseの結果
        results = pose.process(imgRGB)

        resultsF = face.process(imgRGB)

        landNum=0
        if resultsF.multi_face_landmarks:
            for face_landmarks in resultsF.multi_face_landmarks:
                if landNum==0:
                    tmpNum=4
                    preDirection = decidePointDirection([face_landmarks.landmark[tmpNum].x,face_landmarks.landmark[tmpNum].y], img, preDirection, 5)
                    landNum+=1
        #showPoseGUI(results, img, mpDraw, mpPose)
        #w,h = CoGMoved(results,img,mpDraw,mpPose)
        #arrow_trigger=CoGMoved(results, img, arrow_trigger)
        arrow_trigger=Neck_Rotate_inputer(results,img,arrow_trigger)
        #noddRecognition(results,img,w,h)
        # 前の値から今の座標がどちらに移動したかを返す
        #preDirection=decideDirection(results,img,preDirection,5)

        totalD[convertD(preDirection)]+=1
        #print(totalD)
        h, w, c = img.shape  # ウインドウの大きさ
        #cv2.circle(img, (int(results.pose_landmarks.landmark[0].x * w), int(results.pose_landmarks.landmark[0].y * h)), 3, (0, 0, 255), 3)

        dD.append(preDirection)
        if CNT%dDsize==dDsize-2:
            print(dDconvertTotal(dD))
            cntNoddAndRefuse(dDconvertTotal(dD))
        #if stayCounter(keepShoulderPosition(results,w,h,0),5):
        cv2.putText(img, str(CNT), (int(w * 1 / 5), int(h *5/ 6)), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        pTime=showFpsGUI(img,pTime,frameWidth)
        #img = cv2.resize(img, (frameWidth, frameHeight))

        showNoddAndRefuseCntGUI(img)

        cv2.imshow("Image", img)
        # こいつが書き出し
        out.write(img)
        cv2.waitKey(1)
        #次のループへの準備
        CNT += 1

#始まりでありグローバル変数書くところでもある
if __name__ == "__main__":
    noddCnt = 0
    p1 = [0, 0]
    p2 = [0, 0]
    preNose = [0, 0]
    CNT = 0
    shoulderBase = 0
    noseBase = 0
    noddFlag = False
    noddTmp = 0
    refuseTmp = 0
    preNoddX = 0
    totalFPS = 0
    main()
