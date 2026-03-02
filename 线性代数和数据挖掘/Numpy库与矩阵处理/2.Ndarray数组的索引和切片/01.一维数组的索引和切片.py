import numpy as np

arr = np.array([1,2,3,4,5,6])

arr1 = arr[2:4]

"""
    切片操作原数组是不会改变的
"""
print(arr)      #[1 2 3 4 5 6]
print(arr1)     #[3 4]
