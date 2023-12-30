import numpy as np
import matplotlib.pyplot as plt 
import japanize_matplotlib

c_good = np.load('c_good.npy')
c_good_timer_ = np.load("c_good_time.npy")

c_bad = np.load('c_bad.npy')
c_bad_timer_ = np.load("c_bad_time.npy")


c_good_timer_ = c_good_timer_ / max(c_good_timer_)
c_bad_timer_ = c_bad_timer_ / max(c_bad_timer_)

plt.title("バーベルの左右ブレ")
plt.ylabel("左右のずれ[cm]")
plt.xlabel("time")
plt.plot(c_good_timer_, c_good, label = "正しいフォーム")
plt.plot(c_bad_timer_, c_bad, label = "悪いフォーム")
plt.legend()
plt.grid(True)
plt.show()

