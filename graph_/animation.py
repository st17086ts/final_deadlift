#animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import os
import cv2
import time

#動画を取った場合、その動画のFPSを取得する、特に無い場合は独自でFPSを決めてください
cap = cv2.VideoCapture("research_data_\deadlift_edit\B\B_side_open.avi")
fps = cap.get(cv2.CAP_PROP_FPS)
#print(fps)

#csvファイルを読み込む
filepath = "research_data_\deadlift_edit\csv_side\\E_side_degree.csv"
csv_data = pd.read_csv(filepath)

#取り出したいデータのリストを作成する
X_wrist = csv_data["left_hip_deg"]
Y_wrist = csv_data["left_knee_deg"]

#CSVファイルのフレーム数を取得する *欠損ファイルがあったりする場合は注意！
length = len(X_wrist)

# フィギュアオブジェクトの生成やら、幅の間隔の調整
fig = plt.figure()
plt.subplots_adjust(wspace=0.4, hspace=0.5)

#表示したいグラフの個数とかを宣言する　
# (x, y, z）x* y個のグラフを並べた上で、z番目のグラフを作成
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

#描画する関数
def update_func(i):
    # 前のフレームで描画されたグラフを消去、及び出力したいデータをグローバルで持ってくる
    global X_wrist,Y_wrist, length
    ax1.clear()
    ax2.clear()

    #引数で与えられたフレームまで時系列で出力する
    frames = [f for f in range(i)]
    ax1.plot(frames, X_wrist[0:i], color = "black", label = "X_wrist")
    ax2.plot(frames, Y_wrist[0:i], color = "red", label = "Y_wrist")

    #時系列の場合、Xの範囲をあらかじめ決めておいた方がいいよ
    ax1.set_xlim(0, length)
    ax2.set_xlim(0, length)

    ax1.set_xlabel("frames")
    ax2.set_xlabel("frames")
    ax1.set_ylabel("hip")
    ax2.set_ylabel("knee")

    ax1.grid(True)
    ax2.grid(True)

    # サブプロットタイトルの設定
    ax1.set_title('frame: ' + str(i))
    ax2.set_title("frame: " + str(i))

#アニメーション処理
#引数：フィギュアオブジェクト、描画関数（コールバック関数、引数に現在のフレーム数が連番で渡される）、総フレーム数、１フレーム当たり何ミリ秒、リピートするか否か
ani = animation.FuncAnimation(fig, update_func, frames=length, interval=1000/fps , repeat=True)

#表示
plt.show()

#作成したアニメーションを保存、writerにffmpegを指定（うまくいかない場合はffmpegのパスを確認すること）
ani.save("E.mp4", writer = "ffmpeg")

