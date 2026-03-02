# arange函数跟range函数用法几乎一模一样
# arange(,,)中有三个参数：
#                       1.起始位置
#                       2.终止位置
#                       3.步长，默认为1
# 注意:包头不包尾！
# arrange函数适用于创建一维数组
import numpy as np

# arange函数创建0-9数组
arr = np.arange(10)

print(arr)

arr = np.arange(0, 1, 0.1)

print(arr)

# 指定数据类型
arr = np.arange(10, dtype=np.float32)
print(arr)