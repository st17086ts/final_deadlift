#散布図を描画する

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy.optimize as optimize
import sklearn.metrics as metrics
import math
import japanize_matplotlib

file_path = "決定係数のグラフ\\異種混合\\csv\\"

csv_files = []
title = []
for path in os.listdir(file_path):
    csv_files.append(pd.read_csv(file_path + path))
    title.append(path)


def func(X, a, b): # １次式近似
    Y = a + b * X
    return Y




title = ["A", "B", "C", "D", "E"]
for i in range(5):
    plt.title(title[i], fontsize = 25)
    plt.xlim(0, 180)
    plt.ylim(0, 180)
    #print(title[i])
    plt.xlabel("股関節の角度:θw", fontsize = 20)
    plt.ylabel("膝関節の角度:θk", fontsize = 20)
    plt.minorticks_on()
    plt.grid(True) # 目盛線表示
    plt.tick_params(labelsize = 18) # 目盛線ラベルサイズ
    popt, _ = optimize.curve_fit(func, csv_files[i]["left_hip_deg"], csv_files[i]["left_knee_deg"])
    r2 = metrics.r2_score(csv_files[i]["left_knee_deg"], func(csv_files[i]["left_hip_deg"], *popt))
    print(r2)
    
    plt.scatter(csv_files[i]["left_hip_deg"], csv_files[i]["left_knee_deg"])
    theta1, theta0 = np.polyfit(csv_files[i]["left_hip_deg"], csv_files[i]["left_knee_deg"], 1)
    x = np.arange(csv_files[i]["right_hip_deg"].min(), (csv_files[i]["right_hip_deg"].max()))
    y = theta0 + theta1 * x
    plt.plot(x, y, color = "red",lw = 3)
    #print(min(x))

        
    
    plt.show()
