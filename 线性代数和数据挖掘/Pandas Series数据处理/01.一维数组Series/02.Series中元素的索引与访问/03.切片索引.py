import pandas as pd

Series1 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])

# 位置切片  ->  左闭右开
print(Series1[0:3])

# 标签切片  ->  左右两端都闭合
print(Series1['a':'d'])