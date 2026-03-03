import numpy as np

# 函数原型
# numpy.squeeze(a,axis)
# 其中a表示要操作的原始数组，axis表示压缩的指定轴，可以是一个整数或者整数元组
arr = np.array([[[1],[2],[3]]])

print(arr.shape)    # 形状（1,3,1）

# 压缩维度
# 注意：不修改原始数组

# 去掉所有为1的维度
arr1 = np.squeeze(arr)

print(arr)

print(arr1.shape)

print("-"*50)

# 压缩指定轴
# 注意：如果压缩指定位置不为1的轴，会报错！
arr2 = np.squeeze(arr,axis=0)

print(arr2.shape)

arr3 = np.squeeze(arr,axis=(0,2))
print(arr3.shape)