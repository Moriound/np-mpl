import numpy as np

"""
NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。
ndarray 对象是用于存放同类型元素的多维数组。
ndarray 中的每个元素在内存中都有相同存储大小的区域。

ndarray 内部由以下内容组成：
    一个指向数据（内存或内存映射文件中的一块数据）的指针。   
    数据类型或 dtype，描述在数组中的固定大小值的格子。   
    一个表示数组形状（shape）的元组，表示各维度大小的元组。  
    一个跨度元组（stride），其中的整数指的是为了前进到当前维度下一个元素需要"跨过"的字节数。
    跨度可以是负数，这样会使数组在内存中后向移动，切片中 obj[::-1] 或 obj[:,::-1] 就是如此。

创建一个 ndarray 只需调用 NumPy 的 array 函数即可：
"""

# 创建 ndarray
# numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

# 一维
a1 = np.array([1, 2])
print('一维:\n', a1)
print('----------------------------\n')

# 二维
a2 = np.array([[1, 2], [3, 4]])
print('二维:\n', a2)
print('----------------------------\n')

# 参数 dtype 数据类型
# int/uint 8 16 32 64 float 16 32 64 complex 64 128 bool
# 通过np.type可以调用，或者'type' 简写 i1-4 f4 f8 c b u  简写+位数/16
a3 = np.array([-1, 0, 1], dtype='f8')
print('dtype:\n', a3)
print('type:', a3.dtype)
print('----------------------------\n')

# 参数 ndmin 最小维度
a4 = np.array([1, 2, 3], ndmin=3)
print('ndmin:\n', a4)
print('----------------------------\n')

# 结构化数据类型

dt = np.dtype([('name', 'O'), ('age', 'uint8'), ('grade', np.float32)])
print('dt:\n', dt)

a5 = np.array([("还会", 18, 60.5), ('嘿嘿嘿', 66, 50.5), ("666", 12, 99.5), ], dtype=dt)
print('a5:\n', a5)
# 字典式调用
print('a5["age"]:\n', a5['age'])
print('a5["name"]:\n', a5['name'])
print('a5["grade"]:\n', a5['grade'])
print("----------------------------\n")

# numpy array 属性
"""
 秩-rank = 维数-dimensions = 轴-axis
"""

l6 = [[1, 2, 3], [1, 2, 3 + 1j]]
a6 = np.array(l6, 'complex128')

print('a6:\n', a6)
print("dimension:\n", a6.ndim)  # 维数
print('nd.size:\n', a6.size)  # 大小
print('nd.shape:\n', a6.shape)  # 几行几列
print('nd.itemsize:\n', a6.itemsize)  # 每个元素的大小，以字节为单位
print('nd.flags:\n', a6.flags)  # 内存信息
print('nd.real:\n', a6.real)  # 实部
print('nd.imag:\n', a6.imag)  # 虚部
print('nd.data:\n', a6.data)  # 包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

# 创建数组的方式
"""
np.array 给定数据创建
np.empty，np.zeros，np.ones 创建指定大小数组 分别填充 随机数字，0，1
    共有参数 shape:数组行列大小 dtype:数组元素类型 order:'C'(默认)/'F' 行/列优先
"""

a7 = np.empty([2, 3], 'i4')
print('a7:\n', a7)

a8 = np.zeros([2, 3], 'i4')
print('a8:\n', a8)

a9 = np.ones([3, 3], 'i4')
print('a9:\n', a9)