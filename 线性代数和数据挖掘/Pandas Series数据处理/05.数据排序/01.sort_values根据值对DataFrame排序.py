import numpy as np
import pandas as pd
# 创建一个示例 DataFrame
df = pd.DataFrame({
    'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']
})
print(df)
#  A     2     0    a
#  A     1     1    B
#  B     9     9    c
#NaN     8     4    D
#  D     7     2    e
#  C     4     3    F
# 根据 'col1' 列对DataFrame进行排序
res1 = df.sort_values(by=['col1'])
# 打印排序后的DataFrame
print(res1)
# 根据 'col1' 和 'col2' 列对DataFrame进行排序
res2 = df.sort_values(by=['col1', 'col2'])
# 打印排序后的DataFrame
print(res2)