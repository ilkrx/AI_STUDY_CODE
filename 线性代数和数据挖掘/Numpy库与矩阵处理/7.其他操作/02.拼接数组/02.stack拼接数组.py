import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# stack函数原型：
# numpy.stack(数组,axis) 从指定轴插入新的维度
# 结果：新的维度结果：数组个数相加
print(arr1.shape)
print(arr2.shape)

arr3 = np.stack((arr1,arr2),axis=0)

print(arr3.shape)