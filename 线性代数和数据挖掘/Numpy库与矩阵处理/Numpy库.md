# Numpy库

## 1. Numpy库

### 1.1 概念

![1772432450014](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772432450014.png)

### 1.2 安装

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
```

## 2. Ndarray和list的区别

![1772432568561](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772432568561.png)

## 3. Ndarray数组的创建

### 3.1 array函数创建

![1772433000277](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772433000277.png)

![1772433021993](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772433021993.png)

### 3.2 arange函数创建

![1772433247219](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772433247219.png)

### 3.3 zeros函数创建

![1772433381674](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772433381674.png)

### 3.4 ones函数创建

![1772433469097](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772433469097.png)

### 3.5 full函数创建

![1772433614521](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772433614521.png)

## 4. Ndarray数组的索引和切片

​	一维数组的切片方式和列表一模一样。

​	索引用来获取数组中的一个特定位置的数，用来进行修改等操作；切片获取一片区域的数。

### 4.1 多维数组的索引和切片

#### 4.4.1 索引

![1772435444153](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772435444153.png)

#### 4.4.2 切片

![1772435709696](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772435709696.png)

## 5. Ndarray数组的属性

​	有很多属性，一般只关注以下几个：

### 5.1 shape

![1772436535829](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772436535829.png)

### 5.2 dtype

![1772436581625](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772436581625.png)

### 5.3 size

![1772436593877](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772436593877.png)

## 6.改变Ndarray数组的数据类型和形状

### 6.1 数据类型的修改

![1772437469470](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772437469470.png)

==注意：跟切片一样，原数组是不会发生改变的，会生成一个新的数组。==

### 6.2 形状的修改

#### 6.2.1 reshape

![1772438980203](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772438980203.png)

#### 6.2.2 resize

![1772439282680](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772439282680.png)

#### 6.2.3 flatten

![1772439528669](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772439528669.png)

#### 6.2.4 T

![1772439661670](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772439661670.png)

## 7.随机Ndarray数组的创建

![1772441723501](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772441723501.png)

### 7.1 random.rand

![1772441812095](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772441812095.png)

### 7.2 random.randn

![1772442408344](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772442408344.png)



![1772442895608](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772442895608.png)

### 7.3 random.randint

![1772443218513](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772443218513.png)

### 7.4 random.uniform

![1772443597293](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772443597293.png)

### 7.5 random.shuffle

![1772443722141](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772443722141.png)

## 8.Ndarray数组的运算

### 8.1 标量和数组的运算

​	在Numpy中，标量和数组的运算内部是依靠广播机制进行的。

#### 8.1.1 加法运算

​	

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

# 每个位置都要加2
b = arr + 2

print(b)
```



#### 8.1.2 减法运算

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

# 每个位置都要减2
b = arr - 2

print(b)
```



#### 8.1.3 乘法运算

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

# 每个位置都要乘2
b = arr * 2

print(b)
```



#### 8.1.4 除法运算

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

# 每个位置都要除以2
# 注意：只要数组中有一个元素是浮点型数据，那么整个数组都是浮点型
b = arr / 2

print(b)
```

​	==注意：只要数组中有一个元素是浮点型数据，那么整个数组都是浮点型==

### 8.2 数组和数组的运算

#### 8.2.1 加法运算

```
import numpy as np

arr1 = np.array([[11,12,13],[14,15,16]])

arr2 = np.array([[1,2,3],[4,5,6]])

# 数组加上数组，每个对应位置相加

arr3 = arr1 + arr2

print(arr3)
```



#### 8.2.2 减法运算

```
import numpy as np

arr1 = np.array([[11,12,13],[14,15,16]])

arr2 = np.array([[1,2,3],[4,5,6]])

# 数组加上数组，每个对应位置相减

arr3 = arr1 - arr2

print(arr3)
```



#### 8.2.3 乘法运算

```
import numpy as np

arr1 = np.array([[11,12,13],[14,15,16]])

arr2 = np.array([[1,2,3],[4,5,6]])

# 数组加上数组，每个对应位置相乘

arr3 = arr1 * arr2

print(arr3)
```



#### 8.2.4 除法运算

```
import numpy as np

arr1 = np.array([[11,12,13],[14,15,16]])

arr2 = np.array([[1,2,3],[4,5,6]])

# 数组加上数组，每个对应位置相除

arr3 = arr1 / arr2

print(arr3)
```

​	==注意：只要数组中有一个元素是浮点型数据，那么整个数组都是浮点型==

### 8.3 广播机制

![1772455713808](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772455713808.png)

![1772456128843](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772456128843.png)

## 9. 其他操作

### 9.1 修改维度

#### 9.1.1 降维

![1772456921468](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772456921468.png)

![1772456995989](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772456995989.png)

```
import numpy as np

# 函数原型
# numpy.squeeze(a,axis)
# 其中a表示要操作的原始数组，axis表示压缩的指定轴，可以是一个整数或者整数元组
arr = np.array([[[1],[2],[3]]])

print(arr.shape)    # 形状（1,3,1）

# 压缩维度
# 注意：不修改原始数组

# 去掉所有为1的维度
arr1 = np.squeeze(arr)

print(arr)

print(arr1.shape)

print("-"*50)

# 压缩指定轴
# 注意：如果压缩指定位置不为1的轴，会报错！
arr2 = np.squeeze(arr,axis=0)

print(arr2.shape)

arr3 = np.squeeze(arr,axis=(0,2))
print(arr3.shape)
```



#### 9.1.2 升维

![1772457802534](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772457802534.png)

```
import numpy as np

# 函数原型：numpy.expand_dims(a,axis)
arr = np.array([1,2,3])

print(arr.shape)

# 在位置0增加一个维度
# 注意：不修改原始数组
arr1 = np.expand_dims(arr,axis=0)

print(arr1.shape)


# 在位置1增加一个维度
arr2 = np.expand_dims(arr,axis=1)
print(arr2.shape)

# axis是整数元组
arr3 = np.expand_dims(arr,axis=(0,1))
print(arr3.shape)

```

### 9.2 拼接数组

#### 9.2.1 concatenate

![1772503125252](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772503125252.png)

```
import numpy as np

# 创建两个数组
arr1 = np.array([[1,2],[3,4]])  # 形状(2,2)
arr2 = np.array([[5,6]])  # 形状(1,2)

# 要求：所有数组除了在指定轴之外的其他维度形状必须相同
# 函数原型：numpy.concatenate(数组，axis)  ->axis表示按照哪个轴进行拼接
# 结果：拼接的轴相加，其他轴不变

print(arr1.shape)
print(arr2.shape)

arr3 = np.concatenate((arr1,arr2),axis=0)

print(arr3.shape)
```



#### 9.2.2 stack

![1772506402570](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772506402570.png)

```
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# stack函数原型：
# numpy.stack(数组,axis) 从指定轴插入新的维度
# 结果：新的维度结果：数组个数相加
print(arr1.shape)
print(arr2.shape)

arr3 = np.stack((arr1,arr2),axis=0)

print(arr3.shape)
```



### 9.3 分割数组

#### 9.3.1 split

![1772506931202](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772506931202.png)

```
import numpy as np

arr = np.array([1,2,3,4,5,6])

# 平均分割三个数组
result1 = np.split(arr,3)

print(result1)

# 按位置分割
result2 = np.split(arr,[2,4])
print(result2)
```



### 9.4 聚合函数

![1772507837639](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772507837639.png)

#### 9.4.1 mean

![1772507921084](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772507921084.png)

```
import numpy as np

# 计算整个数组的平均值
# 一维数组
arr1 = np.array([1,2,3,4,5])

# 计算平均值
result1 = np.mean(arr1)
print(result1)

# 二维数组
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# [1 2 3
#  4 5 6
#  7 8 9]

# 计算平均值
result2 = np.mean(arr2)
print(result2)

# 指定维度:axis为0表示垂直方向
result3 = np.mean(arr2,axis=0)
print(result3)  # [4. 5. 6.]

# 指定维度:axis为1表示水平方向
result4 = np.mean(arr2,axis=1,keepdims=True)
print(result4)  #[2. 5. 8.]  ->   keepdims保留维度的功劳

# 数组为空的情况
arr3 = np.array([])
# result5 = np.mean(arr3)  # 会报错

# 数据有nan的情况
arr4 = np.array([[np.nan,2],[np.nan,4]])

result6 = np.mean(arr4,axis=0)

print(result6)
# 第一列：所有值是nan,均值为nan
# 第二列：(2 + 4)/2

print(np.nan)
```

#### 9.4.2 sum

![1772515136442](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772515136442.png)

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 计算数组总和
result1 = np.sum(arr)

print(result1)

# 计算每一列的和
result2 = np.sum(arr,axis=0)

print(result2)

# 计算每一行的和
result3 = np.sum(arr,axis=1)

print(result3)

# 保留原始维度
result4 = np.sum(arr,axis=1,keepdims=True)

print(result4)
```

#### 9.4.3 max和min

![1772515488067](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772515488067.png)

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# [1 2 3
#  4 5 6
#  7 8 9]
# 计算数组最大值
result1 = np.max(arr)

print(result1)

# 计算每一列的最大值
result2 = np.max(arr,axis=0)

print(result2)

# 计算每一行的最大值
result3 = np.max(arr,axis=1)

print(result3)

# 保留原始维度
result4 = np.max(arr,axis=1,keepdims=True)

print(result4)
```

![1772516362991](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772516362991.png)

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# [1 2 3
#  4 5 6
#  7 8 9]
# 计算数组最小值
result1 = np.min(arr)

print(result1)

# 计算每一列的最小值
result2 = np.min(arr,axis=0)

print(result2)

# 计算每一行的最小值
result3 = np.min(arr,axis=1)

print(result3)

# 保留原始维度
result4 = np.min(arr,axis=1,keepdims=True)

print(result4)
```

#### 9.4.5 Var

![1772528714101](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772528714101.png)

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 计算数组方差
result1 = np.var(arr)

print(result1)

# 计算每一列的方差
result2 = np.var(arr,axis=0)

print(result2)

# 计算每一行的方差
result3 = np.var(arr,axis=1)

print(result3)

# 保留原始维度
result4 = np.var(arr,axis=1,keepdims=False)

print(result4)
```

#### 9.4.6 std

![1772528821468](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772528821468.png)

```
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# 计算数组标准差
result1 = np.std(arr)

print(result1)

# 计算每一列的标准差
result2 = np.std(arr,axis=0)

print(result2)

# 计算每一行的标准差
result3 = np.std(arr,axis=1)

print(result3)

# 保留原始维度
result4 = np.std(arr,axis=1,keepdims=True)

print(result4)
```

#### 9.4.7 argmax和argmin

![1772528998658](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772528998658.png)

```
import numpy as np
arr = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
print(arr)
# 找出整个数组中的最大值和最小值的索引位置
max_index = np.argmax(arr)
min_index = np.argmin(arr)
# 找出每一列中的最大值和最小值的索引位置
max_index_col = np.argmax(arr, axis=0)
min_index_col = np.argmin(arr, axis=0)
# 找出每一行中的最大值和最小值的索引位置
max_index_row = np.argmax(arr, axis=1)
min_index_row = np.argmin(arr, axis=1)
print(max_index)
print(min_index)

print(max_index_col)
print(min_index_col)
print(max_index_row)
print(min_index_row)
```

### 9.5 where

![1772529096852](C:\Users\Angel\AppData\Roaming\Typora\typora-user-images\1772529096852.png)

```
import numpy as np
# 1、根据条件返回元素的索引
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# 找到大于 5 的元素的索引
print(arr > 5)  # 根据True寻找索引
indices = np.where(arr > 5)

print("大于 5 的元素索引:", indices)


# 2、根据条件选择元素
arr = np.array([1, 2, 3, 4, 5])

# 如果元素大于 3，返回 "大于 3"，否则返回 "小于等于 3"
result = np.where(arr > 3, "大于 3", "小于等于 3")

print(result)



arr = np.array([1, 2, 3, 4, 5])

# 将大于 3 的元素替换为 10，其他元素保持不变
modified_arr = np.where(arr > 3, 10, arr)

print(modified_arr)
```

