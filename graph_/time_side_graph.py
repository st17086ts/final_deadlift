#散布図を描画する
#バーベル写真、グラフ
#背景目的は最後、方法実験、考察でいえることを目的に書く
#今回の結果を利用する

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy.optimize as optimize
import sklearn.metrics as metrics
import math
import japanize_matplotlib

def frame_to_time(frames, fps):
    seconds = []
    for i in range(frames):
        seconds.append(i*(1/fps))

    return seconds


file_path = "..\\judge\膝関節のグラフ\正しい\\csv\\"

csv_files = []
title = []
for path in os.listdir(file_path):
    csv_files.append(pd.read_csv(file_path + path))
    title.append(path)

fps = 30

title = ["A", "B", "C", "D", "E"]

for i in range(5):
    #plt.title(title[i] + "さんの膝関節の時系列グラフ", fontsize = 25)
    print(title[i])
    plt.title(title[i], fontsize = 25)
    plt.xlabel("秒[s]", fontsize = 20)
    plt.ylabel("膝関節の角度（°）:θk", fontsize = 20)

    plt.ylim(75,180)
    plt.minorticks_on()
    

    seconds = frame_to_time(len(csv_files[i]["left_knee_deg"]), fps)
    #plt.xticks(np.arange(0, max(seconds), step=2))
    plt.yticks(np.arange(75, 180, step=10))
    plt.grid(True) # 目盛線表示
    plt.tick_params(labelsize = 18) # 目盛線ラベルサイズ
    data = np.array(csv_files[i]["left_knee_deg"])
    data = np.ma.masked_where(data < 80, data)
    plt.plot(seconds, data)
    #plt.plot(csv_files[i]["left_knee_deg"])
    plt.show()



