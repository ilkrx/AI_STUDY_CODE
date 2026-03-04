import pandas as pd

data = 0

# 第一个参数data是要作为Series数据的值
# 第二个参数index表示值对应的索引
# 注意：
#      索引和值必须一一对应，不能出现索引没有值有和索引有值没有的现象
#      但是！用标量创建可以。表现就是值复制传递下去
Sreies1 = pd.Series(data,index=['a','b'])

print(Sreies1)