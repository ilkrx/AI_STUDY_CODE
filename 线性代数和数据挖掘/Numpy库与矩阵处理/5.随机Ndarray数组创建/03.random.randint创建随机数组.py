import numpy as np

# 注意：只能生成整数
# 生成一个1-10随机数
arr = np.random.randint(1,10)
print(arr)

# 生成一个0-10随机数
arr = np.random.randint(10)
print(arr)

# 生成矩阵
arr = np.random.randint(1,10,(2,3))
print(arr)