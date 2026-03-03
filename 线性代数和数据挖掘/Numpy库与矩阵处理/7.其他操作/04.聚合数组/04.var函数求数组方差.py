import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 计算数组方差
result1 = np.var(arr)

print(result1)

# 计算每一列的方差
result2 = np.var(arr,axis=0)

print(result2)

# 计算每一行的方差
result3 = np.var(arr,axis=1)

print(result3)

# 保留原始维度
result4 = np.var(arr,axis=1,keepdims=False)

print(result4)