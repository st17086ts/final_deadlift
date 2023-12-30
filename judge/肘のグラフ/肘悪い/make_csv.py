#for openpose
#右はopenposeでの右座標をちゃんと使うこと
#このプログラムはcsvファイルを作成するだけに限る

import math
import pandas as pd
import numpy as np
import os
import re
import json
import matplotlib.pyplot as plt
import japanize_matplotlib

name = "太田_正面_肘悪い"
KEYPOINT = 25
file_dir = "太田" 
file_path = file_dir + "\\"

before = 0


#角度の計算, p2p1, p2p3のなす角度を出力する
#もし、出力がうまくいかなければ前回の結果を保持しているbeforeを出力する
#出力は0~180
def calculate_deg(p1, p2, p3):
    global before
    if p1 == None or p2 == None or p3 == None:
        return before
    P2P1 = [x - y for (x, y) in zip(p1, p2)]
    P2P3 = [x - y for (x, y) in zip(p3, p2)]
    innerAB = P2P1[0]*P2P3[0] + P2P1[1]*P2P3[1]
    sA  = P2P1[0]*P2P1[0] + P2P1[1]*P2P1[1]
    sB  = P2P3[0]*P2P3[0] + P2P3[1]*P2P3[1]
    if innerAB != 0:
        cos = innerAB / math.sqrt(sA*sB)
        before = cos
    else: 
        cos = before 
    #print(cos)
    return np.degrees(np.arccos(cos))

def ratio(length1, length2):
    if length2 == 0:
        return -1
    return length1 / length2

def calculate_distance(x1, x2):
    return abs(x1- x2)

#フレーム数確認のためのカウンター
counter = 0

#角度を格納
right_hip_deg = []
left_hip_deg = []
right_knee_deg = []
left_knee_deg = []
right_arm_deg = []
left_arm_deg = []

#比率　肩幅判定に使うやつ
h_s_ratio = []



#jsonファイルを逐次読み込み、角度を計算
for path in os.listdir(file_path):
    if(re.search("json", path)):
        with open(file_path + path) as f:
            #json_data.append(json.load(f))
            tmp = json.load(f)
        x = []
        y = []
        for i in range(KEYPOINT):
            if(len(tmp["people"]) > 0):
                x.append(tmp["people"][-1]["pose_keypoints_2d"][i*3])
                y.append(-tmp["people"][-1]["pose_keypoints_2d"][i*3 + 1])
            else:
                x.append(0)
                y.append(0)

        #5 l shoulder
        #5, 12 ,13
        left_hip_deg.append(calculate_deg((x[5],y[5]), (x[12], y[12]), (x[13], y[13])))
        
        right_hip_deg.append(calculate_deg((x[2],y[2]), (x[9], y[9]), (x[10], y[10])))

        #12, 13, 14
        left_knee_deg.append(calculate_deg((x[12],y[12]), (x[13], y[13]), (x[14], y[14])))
        #9, 10, 11
        right_knee_deg.append(calculate_deg((x[9],y[9]), (x[10], y[10]), (x[11], y[11])))

        #arm
        left_arm_deg.append(calculate_deg((x[5],y[5]), (x[6], y[6]), (x[7], y[7])))
        right_arm_deg.append(calculate_deg((x[2],y[2]), (x[3], y[3]), (x[4], y[4])))

        #ratio hand / shoulder
        h_s_ratio.append(ratio(calculate_distance(x[4], x[7]), calculate_distance(x[2], x[5])))

        #print(right_knee_deg)
        #plt.plot(counter, right_waist_deg)
        counter = counter + 1



data = pd.DataFrame({
        'right_hip_deg' : right_hip_deg,
        'left_hip_deg' : left_hip_deg,
        'right_knee_deg' : right_knee_deg,
        'left_knee_deg' : left_knee_deg,
        'right_arm_deg' : right_arm_deg,
        'left_arm_deg' : left_arm_deg,
        'h_s_ratio' : h_s_ratio
    })

#保存先の指定
data.to_csv("csv\\" + name +"_degree.csv")


