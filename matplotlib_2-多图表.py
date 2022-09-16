import random
import threading
import time
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams['figure.figsize'] = (12.8, 7.2)



fig, axes = plt.subplots(2, 3, figsize=(10.8, 7.2), )  # sharex='all', sharey='all'
fig.suptitle("multi charts")

# 图一
x = []
y = []
x2 = []
y2 = []
for i in range(100001):
    x.append(-1 + i / 100000.0)
    y.append(np.sqrt(1 - x[i] * x[i]))
    x2.append(1 - i / 100000.0)
    y2.append(-np.sqrt(1 - x[i] * x[i]))

axes[0][0].set_title("x^2 + y^2 = 1")
axes[0][0].plot(x, y)
axes[0][0].plot(x2, y)
axes[0][0].plot(x2, y2)
axes[0][0].plot(x, y2)

# 图二
x = np.arange(0, 2, 0.01)
ax = axes[0][1]
ax.plot(x, np.sqrt(x), x, x * x, x, np.power(x, 3))
ax.set_title("y=sqrt(x), x^2, x^3")
ax.legend(['sqrt(x)', 'x^2', 'x^3'])

# 图三
x = ['a', 'b', 'c']
y = [6, 2, 4]

ax = axes[0][2]
ax.set_title("bar chart")
ax.bar(x[0], y[0], color='lightGreen')
ax.bar(x[1], y[1])
ax.bar(x[2], y[2])

ax.legend(x)

# 图四
ax = axes[1][0]
ax.pie(y)
ax.legend(x)
ax.set_title("pie chart")

# 图五
x = np.arange(0, 10, 0.1)
y = [i / 2.0 + random.randint(-100, 100) / 100.0 for i in x]

ax = axes[1][1]
ax.scatter(x, y)
ax.set_title("scatter chart")

# 图六
x = np.linspace(0, np.pi * 2, 200)
y = np.sin(63.5 * x)

# ax = plt.subplot(236, projection='polar')

ax = plt.subplot(236, projection='polar')
ax.plot(x, y)

plt.show()



