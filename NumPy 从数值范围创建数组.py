import numpy as np
"""
np.arange(start=0, stop, step=1, dtype=type(stop)) #不包括stop
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
"""
# np.arange
a1= np.arange(1, 10, 2)
print(a1)

# 使用dtype
a2 = np.arange(1, 10, 2, 'float')
print(a2)

# np.linspace 等差数列
a3 = np.linspace(1, 10, num=10, dtype='i')
print(a3)

# 使用retstep
# a4 = np.linspace(1, 10, num=9, dtype='f', retstep=True) # 显示更多的数组信息，包括公差
# print(a4)

# np.logspace 等比数列
a3 = np.logspace(1, 6, num=10, dtype='float64', base=2)
print(a3)

