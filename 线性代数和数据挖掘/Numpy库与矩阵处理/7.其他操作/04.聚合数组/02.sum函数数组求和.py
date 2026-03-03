import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 计算数组总和
result1 = np.sum(arr)

print(result1)

# 计算每一列的和
result2 = np.sum(arr,axis=0)

print(result2)

# 计算每一行的和
result3 = np.sum(arr,axis=1)

print(result3)

# 保留原始维度
result4 = np.sum(arr,axis=1,keepdims=True)

print(result4)