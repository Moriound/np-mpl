# matplotlib 3D绘图

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

cor = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

# 创建画布
fig = plt.figure()
# set fig title
fig.suptitle("figure 1")

# 使用 add_subplot(row,col,order,projection='3d' ) 创建几行几列序号为order的3D图
axis1 = fig.add_subplot(1, 1, 1, projection="3d")
# axis2 = fig.add_subplot(1, 2, 2)

# 设置x,y,z坐标轴数值范围
axis1.set_xlim(-4, 4)
axis1.set_ylim(-4, 4)
axis1.set_zlim(0, 6)

# set axis label
axis1.set_xlabel("x")
axis1.set_ylabel("y")
axis1.set_zlabel("z")

# set axis1's title
axis1.set_title("3D Graph 1")

z = np.linspace(0, 5, 150)
x = np.sin(z * 20) * z
y = np.cos(z * 20) * z

# using the following function to plot data
# Axes3D.plot(self, xs, ys, *args, zdir='z', **kwargs)
# *args之一  color :'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'
#           line style  '-' '*' '.' '+' or ‘dashdot’ ...
#           linewidth  type: float

axis1.plot(x, y, z, 'b', linewidth=0.5)

# plt.axis("off")  # 隐藏坐标轴
plt.show()
