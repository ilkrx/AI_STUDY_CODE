import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# [1 2 3
#  4 5 6
#  7 8 9]
# 计算数组最小值
result1 = np.min(arr)

print(result1)

# 计算每一列的最小值
result2 = np.min(arr,axis=0)

print(result2)

# 计算每一行的最小值
result3 = np.min(arr,axis=1)

print(result3)

# 保留原始维度
result4 = np.min(arr,axis=1,keepdims=True)

print(result4)