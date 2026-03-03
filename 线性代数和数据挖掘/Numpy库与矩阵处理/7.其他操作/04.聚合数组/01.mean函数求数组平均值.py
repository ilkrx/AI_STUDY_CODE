import numpy as np

# 计算整个数组的平均值
# 一维数组
arr1 = np.array([1,2,3,4,5])

# 计算平均值
result1 = np.mean(arr1)
print(result1)

# 二维数组
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# [1 2 3
#  4 5 6
#  7 8 9]

# 计算平均值
result2 = np.mean(arr2)
print(result2)

# 指定维度:axis为0表示垂直方向
result3 = np.mean(arr2,axis=0)
print(result3)  # [4. 5. 6.]

# 指定维度:axis为1表示水平方向
result4 = np.mean(arr2,axis=1,keepdims=True)
print(result4)  #[2. 5. 8.]  ->   keepdims保留维度的功劳

# 数组为空的情况
arr3 = np.array([])
# result5 = np.mean(arr3)  # 会报错

# 数据有nan的情况
arr4 = np.array([[np.nan,2],[np.nan,4]])

result6 = np.mean(arr4,axis=0)

print(result6)
# 第一列：所有值是nan,均值为nan
# 第二列：(2 + 4)/2

print(np.nan)