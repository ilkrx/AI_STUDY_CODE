# Pandas库

## 1.Pandas库简介

### 1.1 Pandas是什么？

![1772594347214](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772594347214.png)

### 1.2 核心

#### 1.2.1 数据结构

![1772594657563](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772594657563.png)

#### 1.2.2 数据操作

![1772594696746](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772594696746.png)

### 1.3 主要特点

![1772594756588](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772594756588.png)

## 2.Pandas库的安装

命令：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
```

## 3.一维数组Series

​	一维数组的结构可以理解成excel中的一列数据。

![1772595060025](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772595060025.png)

### 3.1 Series的创建

![1772605136016](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772605136016.png)

#### 3.1.1 使用标量创建Series

```
import pandas as pd

data = 0

# 第一个参数data是要作为Series数据的值
# 第二个参数index表示值对应的索引
# 注意：
#      索引和值必须一一对应，不能出现索引没有值有和索引有值没有的现象
#      但是！用标量创建可以。表现就是值复制传递下去
Sreies1 = pd.Series(data,index=['a','b'])

print(Sreies1)
```

#### 3.1.2 使用列表或元组创建Series

```
import pandas as pd

# 用列表或元组创建Series，一般用列表
data = [1,2,3,4,5,6]

Series1 = pd.Series(data,index=['a','b','c','d','e','f'])

print(Series1)
```

#### 3.1.3 使用字典创建Series

![1772606660101](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772606660101.png)

```
import pandas as pd

data = {'name':'唐乾','age':23,'gender':'男'}

# 注意：使用字典创建Series时，字典的键就是索引，字典的值就是索引对应的值
#      如果用字典创建Series时，指定了index,那么生成的Series数组中的数据就是以index参数的值为索引，但是索引对应的值为NaN(只要用了index的索引，用几个就几个NaN)
#      其中，NaN表示缺失数据或者无效数据
# Series1 = pd.Series(data)
Series1 = pd.Series(data,index=['a','b','c'])

print(Series1)
```

#### 3.1.4 使用Ndarray创建Series

```
import pandas as pd
import numpy as np

arr = np.array([1,2,3,4,5])

# copy参数设置False时会改变Ndarray原始数据
Series1 = pd.Series(arr,dtype=float,copy=False)
Series1[0] = 10
print(Series1)
print(arr)
```

### 3.2 Series中元素的索引与访问

#### 3.2.1 位置索引

​	位置索引跟访问列表一样。

```
import pandas as pd

Series1 = pd.Series([10,20,30,40,50])

print(Series1)
print(Series1[0])

# 注意：位置索引有个缺陷
#      当标签和位置值一样时，优先标签
Series2 = pd.Series([1,2,3,4,5],index=[5,4,3,2,1])
print(Series2)
print(Series2[2])
```

#### 3.2.2 标签索引

```
import pandas as pd

Series1 = pd.Series([10,20,30,40,50],index=['a','b','c','d',0])

print(Series1)
print(Series1['c'])
print(Series1[0])
```

#### 3.2.3 切片索引

![1772609199396](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772609199396.png)

```
import pandas as pd

Series1 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])

# 位置切片  ->  左闭右开
print(Series1[0:3])

# 标签切片  ->  左右两端都闭合
print(Series1['a':'d'])
```

## 4.二维数组DataFrame

![1772612032933](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772612032933.png)

### 4.1 DataFrame的创建

![1772612088367](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772612088367.png)

#### 4.1.1 使用列表创建

```
import pandas as pd

data1 = ['小明','小红','小刚']

df1 = pd.DataFrame(data1,index=['a','b','c'],columns=['姓名'])

print(df1)

# 嵌套列表
data2 = [
    ['小明',20,80],
    ['小红',19,60],
    ['小刚',21,99]
]
df2 = pd.DataFrame(data2,index=['a','b','c'],columns=['姓名','年龄','分数'])
print(df2)


```

#### 4.1.2 使用字典创建

![1772612925568](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772612925568.png)

```
import pandas as pd

# 使用字典创建DataFrame，键作为列名
# 字典的值为列表、数组等可迭代对象，要求：长度要一致！
data = {
    'name':['Tom','Nick','John'],
    'age':[19,20,21]
}

df = pd.DataFrame(data)

print(df)
```

#### 4.1.3 使用Ndarray数组创建

```
import pandas as pd
import numpy as np

# data = np.array([1,2,3,4])
# df = pd.DataFrame(data)
# print(df)

data = np.array(
    [
        ['Tom',19],
        ['Nick',20],
        ['John',21]
    ]
)
df = pd.DataFrame(data)

print(df)
```

#### 4.1.4 使用Series创建

```
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
```

### 4.2 DataFrame的属性

```
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
```

### 4.3 DataFrame中元素的索引与访问

```
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
print(df.iloc[0,0])
print(df.iloc[0:1,0:1])

# head  ->  返回前n行，默认5
print(df.head(2))

# tail  ->  返回后n行，默认5
print(df.tail(1))
```

### 4.4 数据操作

#### 4.4.1 数据清洗(都要创建新的DataFrame)

##### 4.4.1.1 isnull

​	用于检测DataFrame中的缺失值，会返回相同形状的布尔型DataFrame，其中每个元素表示原始DataFrame中相应位置的元素是否是缺失值。

```
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
```

##### 4.4.1.2 dropna

![1772674474995](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772674474995.png)

```
import pandas as pd
import numpy as np
# 创建一个包含缺失值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, np.nan, 6],
    'C': [7, 8, 9]
})

print(df)

df.dropna(inplace=True)

print(df)
```

##### 4.4.1.3 fillna

![1772678048676](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772678048676.png)

```
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
```

##### 4.4.1.4 drop_duplicates

![1772676491329](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772676491329.png)

```
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
```

#### 4.4.2 数据转换

##### 4.4.2.1 replace

![1772692807832](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772692807832.png)

```
import pandas as pd

df = pd.DataFrame(
    {
        'A':[1,2,3,4,5],
        'B':['a','b','c','d','e']
    }
)

print(df)
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# 单一值替换
new_df = df.replace(2,10)

print(new_df)

# 列表替换所有匹配值
new_df1 = df.replace([2,3,'a'],'z')
print(new_df1)

# 字典替换
c_dict = {
    2:200,
    'b':'y'
}
new_df2 = df.replace(c_dict)
print(new_df2)

# 使用正则表达式替换
df = pd.DataFrame({
    'col1': ['apple', 'banana', 'cherry', 'agerape', 'apricote'],
    'col2': ['apple pie', 'banana split', 'cherry tart', 'grape juice', 'apricote jam']
})

res = df.replace(r'^a.*e$','fruit',regex=True)  # regex参数默认为False，只有当使用正则表达式替换时一定要设置regex参数
print(res)
```

##### 4.4.2.2 astype

![1772692877218](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772692877218.png)

```
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
```

#### 4.4.3 数据排序

##### 4.4.3.1 sort_values

![1772693751071](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772693751071.png)

```
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
```

##### 4.4.3.2 sort_index

![1772695582634](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772695582634.png)

```
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
```

#### 4.4.4 数据筛选

```
import pandas as pd
data = {
    '姓名': ['小明', '小红', '小刚'],
    '年龄': [20, 18, 22],
    '成绩': [85, 90, 88]
}
df = pd.DataFrame(data)
print(df)
print(df['成绩'] >= 90)
# 使用布尔索引选择成绩大于或等于90的学生
high_scores = df[df['成绩'] >= 90]
print(high_scores)
```

#### 4.4.5 数据拼接

![1772700649967](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772700649967.png)

```
import pandas as pd
# 创建两个 DataFrame
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'F': ['F4', 'F5', 'F6', 'F7']},
                   index=[4, 5, 6, 7])
# 沿着竖直方向拼接两个DataFrame
result = pd.concat([df1, df2], axis=1)
print(result)
```

### 4.5 统计

#### 4.5.1 count

![1772701113521](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701113521.png)

```
import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame(
    {'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': ['foo', 'bar', 'baz', np.nan]
})
# 计算每列非 NaN 值的数量
count_per_column = df.count()
print("Count per column:")
print(count_per_column)
# 计算每行非 NaN 值的数量
count_per_row = df.count(axis=1)
print("\nCount per row:")
print(count_per_row)
# 只计算数值列的非 NaN 值的数量
count_numeric_only = df.count(numeric_only=True)
print("\nCount numeric only:")
print(count_numeric_only)
```

#### 4.5.2 sum

![1772701337996](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701337996.png)

```
import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, np.nan, 8],
'C': [12, np.nan,np.nan, np.nan]
})
# 计算每列的总和
sum_per_column = df.sum()
print("Sum per column:")
print(sum_per_column)
# 计算每行的总和
sum_per_row = df.sum(axis='columns')
print("\nSum per row:")
print(sum_per_row)
# 只计算数值列的总和
sum_numeric_only = df.sum(numeric_only=True)
print("\nSum numeric only:")
print(sum_numeric_only)
# 使用 min_count 参数
sum_with_min_count = df.sum(min_count=2)
print("\nSum with min_count=2:")
print(sum_with_min_count)
```

#### 4.5.3 mean

![1772701350550](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701350550.png)

```
import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, np.nan, 8],
'C': ['foo', 'bar', 'baz', 'qux'] # 非数值列
})
# 计算每列的平均值
# mean_per_column = df.mean()
# print("Mean per column:")
# print(mean_per_column)
# 计算每行的平均值
# mean_per_row = df.mean(axis='columns')
# print("\nMean per row:")

# print(mean_per_row)
# 只计算数值列的平均值
mean_numeric_only = df.mean(numeric_only=True)
print("\nMean numeric only:")
print(mean_numeric_only)
```

#### 4.5.4 median

![1772701362363](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701362363.png)

```
import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
'A': [1, 2, np.nan, 4],
'B': [5, np.nan, 7, 8],
'C': [12, 33, 1, 6] # 非数值列
})
# 计算每列的中位数
median_per_column = df.median()
print("Median per column:")
print(median_per_column)
# 计算每行的中位数
median_per_row = df.median(axis='columns')
print("\nMedian per row:")
print(median_per_row)
# 只计算数值列的中位数
median_numeric_only = df.median(numeric_only=True)
print("\nMedian numeric only:")
print(median_numeric_only)
```

#### 4.5.5 min

![1772701370242](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701370242.png)

```
import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    # 'C': ['foo', 'bar', 'baz', 'qux']  # 非数值列
    'C': [32, 10, 0, 1]  # 非数值列
})
# 计算每列的最小值
min_per_column = df.min()
print("Min per column:")
print(min_per_column)
# 计算每行的最小值
min_per_row = df.min(axis='columns')
print("\nMin per row:")
print(min_per_row)
# 只计算数值列的最小值
min_numeric_only = df.min(numeric_only=True)
print("\nMin numeric only:")
print(min_numeric_only)
```

#### 4.5.6 max

![1772701379778](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701379778.png)

```
import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': ['foo', 'bar', 'baz', 'qux']  # 非数值列
})
# 计算每列的最大值
# max_per_column = df.max()
# print("Max per column:")
# print(max_per_column)
# # 计算每行的最大值
# max_per_row = df.max(axis='columns')
# print("\nMax per row:")
# print(max_per_row)
# 只计算数值列的最大值
max_numeric_only = df.max(numeric_only=True)
print("\nMax numeric only:")
print(max_numeric_only)
```

#### 4.5.7 var

![1772701389886](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701389886.png)

```
import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    # 'C': ['foo', 'bar', 'baz', 'qux']  # 非数值列
})
# 计算每列的方差
var_per_column = df.var()
print("Variance per column:")
print(var_per_column)
# 计算每行的方差
var_per_row = df.var(axis='columns')
print("\nVariance per row:")
print(var_per_row)
# 只计算数值列的方差，并且使用无偏估计（ddof=1）
var_numeric_only = df.var(numeric_only=True, ddof=1)
print("\nVariance numeric only with ddof=1:")
print(var_numeric_only)
```

#### 4.5.8 std

![1772701400027](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701400027.png)

```
import pandas as pd
import numpy as np
# 创建一个包含 NaN 值的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    # 'C': ['foo', 'bar', 'baz', 'qux']  # 非数值列
})
# 计算每列的标准差
std_per_column = df.std()
print("Standard deviation per column:")
print(std_per_column)
# 计算每行的标准差
std_per_row = df.std(axis='columns')
print("\nStandard deviation per row:")
print(std_per_row)
# 只计算数值列的标准差，并且使用无偏估计（ddof=1）
std_numeric_only = df.std(numeric_only=True, ddof=1)
print("\nStandard deviation numeric only with ddof=1:")
print(std_numeric_only)
```

#### 4.5.9 quantile

![1772701411684](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701411684.png)

```
import pandas as pd
# 创建一个DataFrame
data = {
    'col1': [10, 20, 30, 40, 50],
    'col2': [15, 25, 35, 45, 55],
    'col3': [20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
# 按列方向计算0.5分位数（中位数）
col_median = df.quantile(0.5, axis=0)
print("按列方向的0.5分位数（中位数）:\n", col_median)
# 按行方向计算0.5分位数（中位数）
row_median = df.quantile(0.5, axis=1)
print("按行方向的0.5分位数（中位数）:\n", row_median)

```

#### 4.5.10 cummax

![1772701421882](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701421882.png)

```
import pandas as pd
import numpy as np
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 3, 2, 1],
})
# 计算每列的累积最大值
cummax_per_column = df.cummax(axis=0)
print("Cumulative max per column:")
print(cummax_per_column)
# 计算每行的累积最大值
cummax_per_row = df.cummax(axis=1)
print("\nCumulative max per row:")
print(cummax_per_row)
```

#### 4.5.11 cummin

![1772701429923](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701429923.png)

```
import pandas as pd
import numpy as np
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [3, 2, np.nan, 4, 1],
    'B': [5, np.nan, 3, 2, 6],
    # 'C': ['foo', 'bar', 'baz', 'qux', 'quux']  # 非数值列
})
# 计算每列的累积最小值
cummin_per_column = df.cummin(axis=0)
print("Cumulative min per column:")
print(cummin_per_column)
# 计算每行的累积最小值
cummin_per_row = df.cummin(axis=1)
print("\nCumulative min per row:")
print(cummin_per_row)
```

#### 4.5.12 cumsum

![1772701439981](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701439981.png)

```
import pandas as pd
import numpy as np
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 3, 2, 6],
    # 'C': ['foo', 'bar', 'baz', 'qux', 'quux']  # 非数值列
})
# 计算每列的累积和
cumsum_per_column = df.cumsum(axis=0)
print("Cumulative sum per column:")
print(cumsum_per_column)
# 计算每行的累积和
cumsum_per_row = df.cumsum(axis=1)
print("\nCumulative sum per row:")
print(cumsum_per_row)
```

#### 4.5.13 cumprod

![1772701448364](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772701448364.png)

```
import pandas as pd
import numpy as np
# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, 3, 2, 6],
    # 'C': ['foo', 'bar', 'baz', 'qux', 'quux']  # 非数值列
})
# 计算每列的累积乘积
cumprod_per_column = df.cumprod(axis=0)
print("Cumulative product per column:")
print(cumprod_per_column)
# 计算每行的累积乘积
cumprod_per_row = df.cumprod(axis=1)
print("\nCumulative product per row:")
print(cumprod_per_row)
```

## 5.保存与读取

### 5.1 to_csv

![1772708944582](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772708944582.png)

```
import pandas as pd
# 创建一个简单的DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [28, 34, 29],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
# 将DataFrame保存为CSV文件
df.to_csv('人员信息.csv', index=False, encoding='utf_8_sig')
```

### 5.2 to_excel

![1772708979318](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772708979318.png)

```
import pandas as pd
# 创建一个简单的DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [28, 34, 29],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
# 将DataFrame保存为Excel文件
df.to_excel('人员信息.xlsx', index=False)
```

### 5.3 read_csv

![1772710594307](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772710594307.png)

```
import pandas as pd

data = pd.read_csv('./人员信息.csv',nrows=1)
print(data)
```

### 5.4 read_excel

![1772709016810](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772709016810.png)

```
import pandas as pd

data = pd.read_excel('./人员信息.xlsx')
print(data)

"""
    https://pandas.pydata.org/pandas-docs/
"""
```