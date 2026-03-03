import numpy as np

# 函数原型：numpy.expand_dims(a,axis)
arr = np.array([1,2,3])

print(arr.shape)

# 在位置0增加一个维度
# 注意：不修改原始数组
arr1 = np.expand_dims(arr,axis=0)

print(arr1.shape)


# 在位置1增加一个维度
arr2 = np.expand_dims(arr,axis=1)
print(arr2.shape)

# axis是整数元组
arr3 = np.expand_dims(arr,axis=(0,1))
print(arr3.shape)
