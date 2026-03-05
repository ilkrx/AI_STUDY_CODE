import pandas as pd
# 创建一个示例 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4.5, 5.5, 6.5],
    'C': ['7', '8', '9']
})
# 打印原始DataFrame
print(df)

# astype修改列的数据类型
print(df['A'].astype(float))

print(df)

# 使用字典将多列转换为不同的数据类型
c = df.astype(
    {'B':int,
     'C':float
     }
)

print(c)