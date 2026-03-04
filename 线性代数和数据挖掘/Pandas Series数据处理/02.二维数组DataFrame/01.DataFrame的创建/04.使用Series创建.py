import pandas as pd

# 方式1：concat拼接方法（推荐）
# 创建三个pandas Series对象
# name参数表示列名
s1 = pd.Series(['小明', '小红', '小刚'], name='姓名')
s2 = pd.Series([20, 18, 22, 0], name='年龄')
s3 = pd.Series([85, 90, 88], name='成绩')
# 使用concat拼接，并指定轴为1
df = pd.concat((s1, s2, s3), axis=1)
# 打印DataFrame对象，查看其内容
print(df)

# 方式2:使用字典
df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)
