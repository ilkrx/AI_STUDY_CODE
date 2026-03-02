import numpy as np

# 生成一个或一组0-1的随机数
# 注意：浮点数

# 设置随机数种子
# np.random.seed(10)

# 括号里面设置的数组形状
# 没填就是标量
arr = np.random.rand()

print(arr)

# 一个数字就是数组
arr = np.random.rand(3)
print(arr)

# 两个数字就是矩阵
arr = np.random.rand(2,3)
print(arr)
