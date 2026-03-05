import pandas as pd
import numpy as np
# 创建一个多级索引的DataFrame
arrays = [np.array(['qux', 'qux', 'foo', 'foo']),
          np.array(['two', 'one', 'two', 'one'])]
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]},index=arrays)
print(df)
# qux two  1  4
#     one  2  3
# foo two  3  2
#     one  4  1
#          A  B

# 按第一层索引升序排序
df_sorted_by_first_level = df.sort_index(level=0)
print(df_sorted_by_first_level)

# 按第二层索引升序排序
df_sorted_by_second_level_desc = df.sort_index(level=1)
print(df_sorted_by_second_level_desc)

# 按整个索引升序排序
df_sorted_by_full_index = df.sort_index(ascending=True)
print(df_sorted_by_full_index)