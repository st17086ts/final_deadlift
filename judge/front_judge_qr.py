import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy.optimize as optimize
import sklearn.metrics as metrics
import math
import japanize_matplotlib


file_path = "肘のグラフ\\肘悪い\\csv\\"

csv_files = []
title = []
for path in os.listdir(file_path):
    csv_files.append(pd.read_csv(file_path + path))
    title.append(path)


ratio_max = 1.85
ratio_min = 1.0
elbow_deg_max = 165
good_counter = 0


for i in range(5):
    elbow_error = False
    ratio_error_1 = False
    ratio_error_2 = False
    good_counter = 0
    
    ave_ratio = sum(csv_files[i]["h_s_ratio"])/len(csv_files[i]["h_s_ratio"])
    ave_right_elbow_deg =  sum(csv_files[i]["right_arm_deg"])/len(csv_files[i]["right_arm_deg"])
    ave_left_elbow_deg = sum(csv_files[i]["left_arm_deg"])/len(csv_files[i]["left_arm_deg"])

    elbow_right_ratio = 0
    elbow_left_ratio = 0
    for r_deg, l_deg in zip(csv_files[i]["right_arm_deg"], csv_files[i]["right_arm_deg"]):
        if r_deg > elbow_deg_max:
            elbow_right_ratio = elbow_right_ratio + 1
        if l_deg > elbow_deg_max:
            elbow_left_ratio = elbow_left_ratio + 1
    
    elbow_left_ratio = elbow_left_ratio/len(csv_files[i]["right_arm_deg"])
    elbow_right_ratio = elbow_right_ratio/len(csv_files[i]["left_arm_deg"])

    print(elbow_right_ratio, elbow_left_ratio)
    #print(ave_ratio)
    hand = np.array(csv_files[i]["h_s_ratio"])
    hand = np.ma.masked_where(hand > 2, hand)
    hand = np.ma.masked_where(hand < 0.1, hand)
    
    plt.plot(hand)
    plt.title(title[i])
    plt.ylim(0, 2)
    plt.show()
    print(np.mean(hand))
    #print(ave_ratio)
    #print(ave_right_elbow_deg)
    #print(ave_left_elbow_deg)

    #手幅が狭い
    if ratio_min > ave_ratio:
        print("手幅が狭いです")
        ratio_error_1 = True
    
    #手幅が広すぎる
    if ratio_max < ave_ratio:
        print("手幅が広いです")
        ratio_error_2 = True
    
    #肘の角度が曲がっている
    if ave_left_elbow_deg < elbow_deg_max or ave_right_elbow_deg < elbow_deg_max:
        print("肘が曲がっているようです")
        elbow_error = True
    
    #if elbow_error&ratio_error_1&ratio_error_2 == False:
        #print("手幅と肘の角度が良好です。") 
    


    


