import pandas as pd

data = {
    '姓名':['小明','小红','小刚'],
    '年龄':[19,20,21],
    '成绩':[80,60,99]
}

# ,columns=['a','b','c']
df = pd.DataFrame(data)
print(df)

# index  ->  返回DataFrame的行索引
print(df.index)

# columns  ->  返回DataFrame的列索引
print(df.columns)

# values  ->  返回DataFrame中数据的Ndarray表示
print(df.values)

# dtypes  ->  返回每列的数据类型
print(df.dtypes)

# shape  ->  返回DataFrame的形状
print(df.shape)

# size  ->  返回DataFrame的元素数量
print(df.size)

# empty  ->  返回DataFrame是否为空
print(df.empty)

# T  ->  返回DataFrame的转置
print(df.T)

# ndim  ->  返回DataFrame的维度数。通常是2
print(df.ndim)