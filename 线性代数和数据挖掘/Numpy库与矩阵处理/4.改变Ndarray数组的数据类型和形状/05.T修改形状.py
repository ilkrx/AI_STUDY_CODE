import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

# T不修改原始数组数据，转置操作

arr1 = arr.T    # 注意：这个T不需要加括号()

print(arr)
print(arr1)