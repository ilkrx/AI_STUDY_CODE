import pandas as pd
import numpy as np
# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})
# 打印原始DataFrame
print(df)
# 使用 isnull() 方法检测缺失值
missing_values = df.isnull()
print(missing_values)