import numpy as np

# 创建一维全为1的数组
# ones函数和zeros函数用法一样，其中dtype参数默认值为float
arr = np.ones(5)
print(arr)

# 创建二维全是1的数组
arr = np.ones((2,3))
print(arr)

# 创建三维全1的数组
arr = np.ones((2,2,3))
print(arr)