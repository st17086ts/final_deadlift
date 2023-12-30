import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import scipy.optimize as optimize
import sklearn.metrics as metrics
import math
import japanize_matplotlib


file_path = "膝関節のグラフ\\正しい\\csv\\"

csv_files = []
title = []
for path in os.listdir(file_path):
    csv_files.append(pd.read_csv(file_path + path))
    title.append(path)


knee_max = 133
good_counter = 0


for i in range(2):
    flag = False
    good_counter = 0
    for deg in csv_files[i]["left_knee_deg"]:
        
        if deg <= knee_max and flag == False:
            good_counter = good_counter + 1
            flag = True
        
        elif deg <= knee_max and flag == True:
            flag = True
            #good_counter = good_counter + 1
        else:
            flag = False

    
    
    
    print(good_counter)
    if good_counter > 5:
        print("good lift")



        


        

