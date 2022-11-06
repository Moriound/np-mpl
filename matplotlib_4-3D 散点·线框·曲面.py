from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(24, 8))

g1 = fig.add_subplot(1, 3, 1, projection='3d')
g2 = fig.add_subplot(1, 3, 2, projection='3d')
g3 = fig.add_subplot(1, 3, 3, projection='3d')


def scatter_3d():
    g1.set_title('scatter')

    x = np.arange(100)
    y = np.random.randint(0, 300, 100)
    z = np.random.randint(0, 200, 100)

    # s：marker标记的大小
    # c: 颜色  可为单个，可为序列
    # depthshade: 是否为散点标记着色以呈现深度外观。对 scatter() 的每次调用都将独立执行其深度着色。
    # marker：样式
    g1.scatter(xs=x, ys=y, zs=z, zdir='z', s=30, c="g", depthshade=True, cmap="jet", marker="*")


def wireframe_3d():
    x, y, z = axes3d.get_test_data(0.05)

    g2.plot_wireframe(x, y, z, color='c')


def surface_3d():
    from matplotlib import cm
    from matplotlib.ticker import LinearLocator

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    surf = g3.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    fig.colorbar(surf, shrink=0.2, aspect=5)


scatter_3d()
wireframe_3d()
surface_3d()

plt.show()
