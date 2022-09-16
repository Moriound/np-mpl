import matplotlib.pyplot as plt
import numpy as np

# test 1
plt.title("learning")
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


