'''
mpiを利用して四つのwindowに分割して表示
'''

from mpi4py import MPI
import cv2
import mediapipe as mp
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
total_cnt=0
# (2)
cnt1=0
start_time = time.time() # start time of the loop

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1
    ) as hands:
  while cap.isOpened():
    success, image = cap.read()
    height, width, channels = image.shape
    #(1)
    if rank==0:
    #image = image[0:height//2,0:width//2]
    #image = image[0:height//2,width//2:width]
        image = image[height//2:height,0:width//2]
    #image = image[height//2:height,width//2:width]
    elif rank==1:
        image = image[0:height//2,width//2:width]
    elif rank==2:
        image = image[height//2:height,width//2:width]
    elif rank==3:
        image = image[0:height//2,0:width//2]
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    if rank==0:
        cv2.imshow('MediaPipe Hands1', cv2.flip(image, 1))
        #(2)
        cnt1+=1
        if (time.time()-start_time)>1:
            print(total_cnt,"FPS: ", cnt1 / (time.time() - start_time)) # FPS = 1 / time to process loop
            cnt1=0
            total_cnt+=1
            start_time=time.time()

    elif rank==1:
        cv2.imshow('MediaPipe Hands2', cv2.flip(image, 1))
    elif rank==2:
        cv2.imshow('MediaPipe Hands3', cv2.flip(image, 1))
    elif rank==3:
        cv2.imshow('MediaPipe Hands4', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
    #print(cap.get(cv2.CAP_PROP_FPS))
cap.release()

#(1) https://qiita.com/kino15/items/56c0fffce4c14a875199
#(2) https://www.webdevqa.jp.net/ja/python/fps%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%82%92%E6%99%82%E9%96%93%E9%96%A2%E6%95%B0%E3%81%A7%E9%99%A4%E7%AE%97%E3%81%97%E3%81%A6fps%E3%82%92%E6%B1%BA%E5%AE%9A%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/832531840/