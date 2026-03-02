import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print(arr)
#resize修改原数组数据

arr.resize((3,2))
print(arr)

arr.resize((2,2))
print(arr)

arr.resize((5,5))
print(arr)
