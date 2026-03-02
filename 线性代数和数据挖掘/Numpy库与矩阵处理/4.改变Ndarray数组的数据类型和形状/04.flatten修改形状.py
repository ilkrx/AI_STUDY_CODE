import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

# flatten不修改原始数组数据,是将数组平铺成一维数组
arr1 = arr.flatten()

print(arr)
print(arr1)