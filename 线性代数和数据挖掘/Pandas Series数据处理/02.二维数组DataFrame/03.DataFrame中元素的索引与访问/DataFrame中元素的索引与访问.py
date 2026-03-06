import pandas as pd

data = {
    '姓名':['小明','小红','小刚'],
    '年龄':[19,20,21],
    '成绩':[80,60,99]
}

df = pd.DataFrame(data)
print(df)

# 使用列名访问
# 返回的是一个Series对象
print(df['姓名'])
# 访问具体值
print(df['年龄'][1])


# loc和iloc方法
# 注意：方法原型：df.loc[]  ->  中括号
# 区别：loc是标签，iloc是索引下标
print(df.loc[0,'姓名'])
# 切片
print(df.loc[0:2,'姓名':'年龄'])
print('-'*30)
print(df.loc[[0,2],['姓名','年龄']])
print(df.iloc[0,0])
print(df.iloc[0:1,0:1])

# # head  ->  返回前n行，默认5
# print(df.head(2))
#
# # tail  ->  返回后n行，默认5
# print(df.tail(1))