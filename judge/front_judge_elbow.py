import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy.optimize as optimize
import sklearn.metrics as metrics
import math
import japanize_matplotlib


file_path = "肘のグラフ\\正しい\\csv\\"

csv_files = []
title = []
for path in os.listdir(file_path):
    csv_files.append(pd.read_csv(file_path + path))
    title.append(path)


def frame_to_time(frames, fps):
    seconds = []
    for i in range(frames):
        seconds.append(i*(1/fps))

    return seconds

ratio_max = 1.85
ratio_min = 1.0
elbow_deg_max = 165
good_counter = 0


for i in range(5):

    
    ave_ratio = sum(csv_files[i]["h_s_ratio"])/len(csv_files[i]["h_s_ratio"])
    ave_right_elbow_deg =  sum(csv_files[i]["right_arm_deg"])/len(csv_files[i]["right_arm_deg"])
    ave_left_elbow_deg = sum(csv_files[i]["left_arm_deg"])/len(csv_files[i]["left_arm_deg"])

    elbow_right_ratio = 0
    elbow_left_ratio = 0
    for r_deg, l_deg in zip(csv_files[i]["right_arm_deg"], csv_files[i]["left_arm_deg"]):
        #print(r_deg, l_deg)
        if r_deg > elbow_deg_max:
            elbow_right_ratio = elbow_right_ratio + 1
        if l_deg > elbow_deg_max:
            elbow_left_ratio = elbow_left_ratio + 1
    
    elbow_left_ratio = elbow_left_ratio/len(csv_files[i]["right_arm_deg"])
    elbow_right_ratio = elbow_right_ratio/len(csv_files[i]["left_arm_deg"])
    print(elbow_left_ratio, elbow_right_ratio)
    
    
    seconds = frame_to_time(len(csv_files[i]["left_knee_deg"]), 30)
    
    plt.title(title[i], fontsize = 11)
    plt.xlabel("時間[s]", fontsize = 11)
    plt.ylabel("肘の角度", fontsize = 11)
    plt.ylim(80, 180)
    plt.plot(seconds, csv_files[i]["right_arm_deg"], label = "右肘の角度")
    plt.plot(seconds, csv_files[i]["left_arm_deg"], label = "左肘の角度")
    
    plt.legend()

    plt.show()
    
    
    #肘の角度が曲がっている
    if ave_left_elbow_deg < elbow_deg_max or ave_right_elbow_deg < elbow_deg_max:
        print("肘が曲がっているようです")
        elbow_error = True
    
    #if elbow_error&ratio_error_1&ratio_error_2 == False:
        #print("手幅と肘の角度が良好です。") 
    


    


