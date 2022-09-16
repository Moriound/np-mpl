import matplotlib.pyplot as plt
import numpy as np

# test 1
"""plt.title("learning")
plt.xlabel("x-x ")
plt.ylabel("y-F(x)")
plt.grid(color='lightgreen', axis='both', linestyle='dashed')

x = np.arange(-6,6, 0.05)
y = np.sin(x)
y2 = np.cos(x)+2
y3 = x[slice(0,40, 5)] + 10

plt.plot(x, y, "b")
plt.plot(y3)
plt.plot(x, y2, linestyle='dashdot', linewidth=10)
plt.show()
"""

# test2
# 多图
# plt.subplots(2, 3)  # 一次创建多图
# plt.subplot(2, 3, 4)  # (几行， 几列，总的第几个)

# 先选择再绘图
plt.subplot(2,3,6)

plt.plot([1,2], [3, 4])

plt.subplot(2,3,1)

x = np.linspace(-5,5,100)
y = np.sin(x)
plt.plot(x, y)

plt.show()
