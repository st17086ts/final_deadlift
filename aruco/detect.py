### マーカーIDと、動画を重ねて表示する
import cv2
from cv2 import aruco
import time
import matplotlib.pyplot as plt
import japanize_matplotlib

### --- aruco設定 --- ###
dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

#cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap = cv2.VideoCapture("..\\research_data_\deadlift_edit\E\E_qr.mov")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # カメラ画像の横幅を1280に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
tracks = []

x = []
y = []
#保存する動画の設定
frame_rate = 30
size = (int(cap.get(3)), int(cap.get(4)))
#fmt = cv2.VideoWriter_fourcc("m", "p", "4", "v")
#writer_video = cv2.VideoWriter("video\\A.mp4", fmt, frame_rate, size)


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

try:
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
            x.append(int(center[0]))
            y.append(int(center[1]))
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
        if cv2.waitKey(1) & 0xFF == ord('q'):
            plt.xlim(0, 1920)
            plt.ylim(0, 1080)
            plt.scatter(x, y)
            plt.xlabel("pixcel", fontsize = 20)
            plt.ylabel("pixcel", fontsize = 20)
            plt.title("Eさんのバーベル軌道", fontsize = 25)
            plt.show()
            seconds = frame_to_seconds(len(x), 30)
            plt.plot(seconds, x)
            plt.plot(seconds, y)
            plt.ylim(0, 1980)
            plt.title("横ブレ", fontsize = 25)
            plt.ylabel("ピクセル", fontsize = 20)
            plt.xlabel("秒", fontsize = 20)
            plt.legend(loc="lower left", fontsize=18) 
            plt.show()
            break
    cv2.destroyWindow('frame')
    #ファイルを閉じる
    #writer_video.release()
    plt.xlim(0, 1920)
    plt.ylim(0, 1080)
    plt.scatter(x, y)
    plt.xlabel("pixcel", fontsize = 20)
    plt.ylabel("pixcel", fontsize = 20)
    plt.title("Eさんのバーベル軌道", fontsize = 25)
    plt.show()
    seconds = frame_to_seconds(len(x), 30)
    plt.plot(seconds, x, label = "x軸のブレ")
    #plt.plot(seconds, y, label = "y軸")
    plt.ylim(0, 1980)
    plt.title("横ブレ", fontsize = 25)
    plt.ylabel("ピクセル", fontsize = 20)
    plt.xlabel("秒", fontsize = 20)
    plt.legend(loc="lower left", fontsize=18) 
    print(max(x) - min(x))
    plt.show()
    result = [n - x[0] for n in x]
    plt.plot(seconds, x)
    plt.title("初期地点の差")
    plt.ylabel("pixcel")
    plt.xlabel("seconds")
    plt.show()
    cap.release()

except KeyboardInterrupt:
    cv2.destroyWindow('frame')
    cap.release()