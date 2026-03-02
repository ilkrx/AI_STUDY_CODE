import numpy as np

# 索引
arr = np.array([[[1,2,3],[4,5,6]],[[1,4,7],[2,5,8]]])
print(arr)

print(arr[0])

print(arr[0][1][2])

print(arr[0,1])

print("-"*50)

# 切片
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr)      #[1,2,3
                # 4,5,6
                # 7,8,9]

#  切行
arr1 = arr[0:2]     #不切列的话，列的位置可以省略

arr2 = arr[0]

print(arr1)     #[123
                # 456]

print(arr2)

#  切列
arr3 = arr[:,0:2]   #不切行的话，行的位置必须用 ：代替
print(arr3)

arr4 = arr[:,[0,2]]     #  切的不是连续的列
print(arr4)

#  又切行又切列
arr5 = arr[0:2,0:2]
print(arr5)         #[1 2
                    # 4 5]