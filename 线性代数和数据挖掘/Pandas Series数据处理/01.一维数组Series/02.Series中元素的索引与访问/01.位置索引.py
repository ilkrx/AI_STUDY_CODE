import pandas as pd

Series1 = pd.Series([10,20,30,40,50])

print(Series1)
print(Series1[0])

# 注意：位置索引有个缺陷
#      当标签和位置值一样时，优先标签
Series2 = pd.Series([1,2,3,4,5],index=[5,4,3,2,1])
print(Series2)
print(Series2[2])