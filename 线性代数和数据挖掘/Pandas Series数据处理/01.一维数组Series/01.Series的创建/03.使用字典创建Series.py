# import pandas as pd
#
# data = {'name':'唐乾','age':23,'gender':'男'}
#
# # 注意：使用字典创建Series时，字典的键就是索引，字典的值就是索引对应的值
# #      如果用字典创建Series时，指定了index,那么生成的Series数组中的数据就是以index参数的值为索引，但是索引对应的值为NaN(只要用了index的索引，用几个就几个NaN)
# #      其中，NaN表示缺失数据或者无效数据
# # Series1 = pd.Series(data)
# Series1 = pd.Series(data,index=['a','b','c'])
#
# print(Series1)
import pandas as pd

dict_message = {
"姓名":"成绩"
}

s = pd.Series(dict_message)
print(s)