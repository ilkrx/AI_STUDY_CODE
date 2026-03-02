import numpy as np

arr = np.array([1.1,1.2,1.3],dtype=np.float64)

# 数据类型的修改Ndarray.astype函数
# 数据类型的修改会产生一个新的数组，原数组是不会发生改变的

arr1 = arr.astype(np.int32)


print(arr)
print(arr.dtype)
print(arr1)
print(arr1.dtype)