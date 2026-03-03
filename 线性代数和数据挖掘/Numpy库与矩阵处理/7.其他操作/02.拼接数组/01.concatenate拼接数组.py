import numpy as np

# 创建两个数组
arr1 = np.array([[1,2],[3,4]])  # 形状(2,2)
arr2 = np.array([[5,6]])  # 形状(1,2)

# 要求：所有数组除了在指定轴之外的其他维度形状必须相同
# 函数原型：numpy.concatenate(数组，axis)  ->axis表示按照哪个轴进行拼接
# 结果：拼接的轴相加，其他轴不变

print(arr1.shape)
print(arr2.shape)

arr3 = np.concatenate((arr1,arr2),axis=0)

print(arr3.shape)
