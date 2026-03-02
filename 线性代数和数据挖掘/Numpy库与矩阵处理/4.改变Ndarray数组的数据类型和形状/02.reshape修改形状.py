import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

#reshape不修改原数组数据

arr1 = arr.reshape((3,2))

print(arr)
print(arr1)