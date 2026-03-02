import numpy as np

# 创建一维全为0的数组
# zeros()函数括号里面表示创建的数组的形状，其中dtype参数默认值为float
arr = np.zeros(5)
print(arr)

# 创建二维全是0的数组
arr = np.zeros((2,3))
print(arr)

# 创建三维全0的数组
arr = np.zeros((2,2,3))
print(arr)