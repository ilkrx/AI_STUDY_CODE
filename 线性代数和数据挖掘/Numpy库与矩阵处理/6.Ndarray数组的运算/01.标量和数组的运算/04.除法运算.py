import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

# 每个位置都要除以2
# 注意：只要数组中有一个元素是浮点型数据，那么整个数组都是浮点型
b = arr / 2

print(b)