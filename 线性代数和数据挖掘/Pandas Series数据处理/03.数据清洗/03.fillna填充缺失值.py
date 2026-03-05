import pandas as pd
import numpy as np
# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [np.nan, np.nan, 6],
    'C': [7, np.nan, 9]
})

print(df)

# 标量填充
df_filled_value = df.fillna(value=1)

print(df_filled_value)

# 前向填充
df_filled_value = df.bfill()
print(df_filled_value)

"""
    指定列标签填充
"""
data = {
    'A': 'a',
    'B': 'b',
    'C': 'c'
}
df_filled_value = df.fillna(value=data)
print(df_filled_value)

"""
    使用 limit 参数
"""

filled_with_limit = df.fillna(value=0, limit=1)
print(filled_with_limit)