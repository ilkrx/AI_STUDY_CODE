import numpy as np

# 用于创建全是同一个数字的数组，例如全是2

arr = np.full(3,3)
print(arr)

arr = np.full((2,3),3)
print(arr)

arr = np.full((2,2,3), 5.5, dtype=float)
print(arr)