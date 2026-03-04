import pandas as pd

# 用列表或元组创建Series，一般用列表
data = [1,2,3,4,5,6]

Series1 = pd.Series(data,index=['a','b','c','d','e','f'])

print(Series1)