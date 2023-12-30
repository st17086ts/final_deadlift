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


file_path = "..\\judge\\手幅のグラフ\\正しい\\csv\\"

csv_files = []
title = []
for path in os.listdir(file_path):
    csv_files.append(pd.read_csv(file_path + path))
    title.append(path)

fps = 60

title = ["A", "B", "C", "D", "E"]
for i in range(5):
    window = 10 # 移動平均の範囲
    w = np.ones(window)/window

    x = np.convolve(csv_files[i]["h_s_ratio"], w, mode='same')
    #print(x)
    plt.title(title[i] + "さんの手幅/肩幅の時系列グラフ", fontsize = 11)
    plt.xlabel("秒[s]", fontsize = 11)
    plt.ylabel("割合", fontsize = 11)

    #plt.ylim(75,180)
    plt.minorticks_on()
    plt.ylim(0, 3)
    data = np.array(csv_files[i]["h_s_ratio"])
    #print(data)
    data = np.ma.masked_where(data > 3,data)
    #print(data)
    data = np.ma.masked_where(data < 0.01, data)
    seconds = frame_to_time(len(csv_files[i]["h_s_ratio"]), fps)
    #plt.xticks(np.arange(0, max(seconds), step=2))
    plt.grid(True) # 目盛線表示
    plt.tick_params(labelsize = 18) # 目盛線ラベルサイズ

    plt.plot(seconds, data)
    #plt.plot(seconds, x, label = "平滑化")
    #plt.plot()
    plt.legend(loc="lower left", fontsize=18) 
    plt.show()


