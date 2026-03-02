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