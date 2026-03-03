import numpy as np

arr = np.array([1,2,3,4,5,6])

# 平均分割三个数组
result1 = np.split(arr,3)

print(result1)

# 按位置分割
result2 = np.split(arr,[2,4])
print(result2)