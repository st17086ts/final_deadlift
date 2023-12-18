#散布図を描画する
#バーベル写真、グラフ
#背景目的は最後、方法実験、考察でいえることを目的に書く
#今回の結果を利用する

#始祖

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy.optimize as optimize
import sklearn.metrics as metrics
import math
import japanize_matplotlib

file_path = "..\\research_data_\\deadlift_edit\\csv_side\\"

csv_files = []
title = []
for path in os.listdir(file_path):
    csv_files.append(pd.read_csv(file_path + path))
    title.append(path)

for i in range(3):
    plt.title(title[i])
    plt.xlabel("frame", fontsize = 10)
    plt.ylabel("膝の角度:θk", fontsize = 10)

    #plt.plot(csv_files[i]["right_hip_deg"])


    plt.grid(True) # 目盛線表示
    plt.tick_params(labelsize = 18) # 目盛線ラベルサイズ

    plt.plot(csv_files[i]["h_s_ratio"])
    plt.show()

    plt.plot(csv_files[i]["right_arm_deg"])
    plt.show()
