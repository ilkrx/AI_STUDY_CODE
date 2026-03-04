import pandas as pd

data1 = ['小明','小红','小刚']

df1 = pd.DataFrame(data1,index=['a','b','c'],columns=['姓名'])

print(df1)

# 嵌套列表
data2 = [
    ['小明',20,80],
    ['小红',19,60],
    ['小刚',21,99]
]
df2 = pd.DataFrame(data2,index=['a','b','c'],columns=['姓名','年龄','分数','2'])
print(df2)

