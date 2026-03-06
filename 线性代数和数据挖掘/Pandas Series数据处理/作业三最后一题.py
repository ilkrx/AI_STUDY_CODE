import pandas as pd
import numpy as np
data = {
    '日期':['2023-01-01','2023-01-01','2023-01-02','2023-01-02','2023-01-03','2023-01-03','2023-01-04','2023-01-04'],
    '产品':['A','B','A','B','A','B','A','B'],
    '销售额':[1200,800,1500,np.nan,1100,950,np.nan,1300],
    '地区':['华北','华东','华北','华东','华北','华东','华北','华东']
}

df = pd.DataFrame(data)
print(df)

# 检测缺失值,统计每列缺失值
print(df.isnull())
print(df.isnull().sum())

# 排序
sort_df = df.sort_values('产品')
print(sort_df)
# 计算平均
mean = sort_df.head(4).mean(numeric_only=True)
print(mean)
print('-'*30)
s1 = sort_df.head(4).fillna(mean,limit=1)
print(s1)

mean = sort_df.tail(4).mean(numeric_only=True)
print(mean)
print('-'*30)
s2 = sort_df.tail(4).fillna(mean,limit=1)
print(s2)

s = pd.concat([s1,s2])
print(s)
print('-'*30)

# 删除
drop_df = df.dropna()
print(drop_df)

sort_df = df.sort_values(['日期','销售额'],ascending=[True,False])
print(sort_df)

# 筛选
condition = (df['销售额'] > 1000) & (df['地区'] == '华北')
filtered_df = df[condition]
print(filtered_df)