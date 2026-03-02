# 导包
import numpy as np

# array函数创建数组：
# def array(p_object, dtype=None, *args, **kwargs)：
# dtype参数：可以指定数组的数据类型，如果未指定，则根据输入数据自行判断
# 创建一维数组
arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr)

# 创建二维数组
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

# 创建三维数组
arr = np.array([[[1,2,3],[4,5,6]]])
print(arr)

# 注意：np.array()  括号里面的参数需要是可迭代的数据类型，如列表或者元组
l1 = [1,2,3,4,5,6,7,8,9]
arr = np.array(l1)
print(arr)
print(type(l1),type(arr))