#散布図を描画する

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


for i in range(1):

    #x軸は股関節
    #x = csv_files[i]["left_hip_deg"]
    #y = csv_files[i]["left_knee_deg"]
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]

    w = np.polyfit(x, y, 1)
    fx = np.poly1d(w)(1)
    print(w)
    plt.scatter(x, y)
    plt.plot(x, fx)
    plt.show()

    upper = 0
    for i in range(len(x)):
        #u = (y[i] - a * x[i] - b)**2
        upper = upper 

    print(upper)

    ave = sum(y)/len(y)
    lowwer = 0
    for i in range(len(x)):
        l = (y[i] -  ave)**2
        lowwer = lowwer + l

    print(lowwer)

    print(1 - upper/lowwer)


    
    
