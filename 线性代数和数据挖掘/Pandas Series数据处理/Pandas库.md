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

