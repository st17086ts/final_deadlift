### マーカーIDと、動画を重ねて表示する
import cv2
from cv2 import aruco
import time
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

### --- aruco設定 --- ###
dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

#cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap = cv2.VideoCapture("バーベル\悪いフォーム\鈴木バーベル.mp4")
tracks = []

x = []
y = []
#保存する動画の設定
frame_rate = 30
size = (int(cap.get(3)), int(cap.get(4)))
#fmt = cv2.VideoWriter_fourcc("m", "p", "4", "v")
#writer_video = cv2.VideoWriter("video\\A.mp4", fmt, frame_rate, size)

def multi(val):
    return val * 0.135



#軌跡を描く関数　(input：　過去の軌跡, 追加する点, フレーム)
def drawObit(tracks, new_point, frame):
    tracks.append(new_point)

    for track in tracks:
        cv2.circle(frame, track, 5, (0, 255, 0), thickness=-1)
    
def frame_to_seconds(frames, fps):
    seconds = []
    s = 0
    for i in range(frames):
        s = s + 1 / fps
        seconds.append(s)
    
    return seconds


timer = 0
time_ = []
    
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    height, width, channels = frame.shape[:3]
    #print("width: " + str(width))
    #print("height: " + str(height))
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dict_aruco, parameters=parameters)
    #print(corners[0][0][0])
    index = 0
    if corners != ():
        cornerUL = corners[index][0][0]
        cornerUR = corners[index][0][1]
        cornerBR = corners[index][0][2]
        cornerBL = corners[index][0][3]
        center = [ (cornerUL[0]+cornerBR[0])/2 , (cornerUL[1]+cornerBR[1])/2 ]
        #drawObit(tracks, (int(corners[0][0][0][0]), int(corners[0][0][0][1])), frame)
        drawObit(tracks, (int(center[0]), int(center[1])), frame)
        if int(center[0]) >= 815  and int(center[0]) <= 1191:
        #if int(center[0]) >= 940  and int(center[0]) <= 1312:
            #print(x)
            x.append(int(center[0]))
            y.append(int(center[1]))
            time_.append(timer)
    else:

        for track in tracks:
            cv2.circle(frame, track, 5, (0, 255, 0), thickness=-1)
    #print(corners)

    if(len(tracks) > 10):
        del tracks[0]

    
    frame_markers = aruco.drawDetectedMarkers(frame, corners, ids)
    frame_markers = cv2.resize(frame_markers, (680, 480))
    cv2.imshow('frame', frame_markers)
    #writer_video.write(frame)
    
    timer = timer + 1 / 30

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(max(x) - min(x))
        if max(x) - min(x) > 200:
            print((max(x) - min(x)) * 0.135)
            print("バーベルと体の距離が遠い可能性があります。もっとひきつけて挙上しましょう。")

        x_centi = map(lambda val: val * 0.135, x)
        x_centi = list(x_centi)

        x_centi_sub = map(lambda val: val - x_centi[0], x_centi)
        x_centi_sub = list(x_centi_sub)

        plt.grid(True)
        plt.scatter(time_,x_centi_sub)
        plt.plot(time_,x_centi_sub)
        plt.ylabel("初期位置との差[cm]", fontsize = 20)
        plt.xlabel("時間[s]", fontsize = 20)
        plt.title("バーベルの左右のブレ(Dさん)", fontsize = 20)
        plt.xlim(0, timer)
        plt.show()
        x = np.array(x_centi_sub)
        time_ = np.array(time_)
        np.save("c_bad", x)
        np.save("c_bad_time", time_)
        break
cv2.destroyWindow('frame')
#ファイルを閉じる
#writer_video.release()
cap.release()



