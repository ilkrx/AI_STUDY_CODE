import pandas as pd
# 创建一个包含重复行的 DataFrame
df = pd.DataFrame({
    'A': [1, 1, 2, 2, 3, 3],
    'B': [1, 1, 2, 2, 3, 3],
    'C': [1, 1, 2, 2, 3, 3]
})
# 打印原始DataFrame
print(df)
# 删除重复行，保留第一次出现的重复项
df_dedup_first = df.drop_duplicates()
print(df_dedup_first)
# 根据指定列删除重复行
df_dedup_column = df.drop_duplicates(subset='A')
print(df_dedup_column)